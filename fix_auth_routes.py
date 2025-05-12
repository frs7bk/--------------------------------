
# إصلاح مشاكل مسارات المصادقة
import logging
import os
from flask import redirect, url_for, flash, request, session
from functools import wraps

logger = logging.getLogger(__name__)

def fix_auth_routes():
    """إصلاح مشاكل مسارات المصادقة"""
    try:
        from auth_routes import login, register
        from flask_login import login_user, current_user
        from models import User
        from werkzeug.security import check_password_hash
        
        # تعديل دالة تسجيل الدخول
        def fixed_login():
            if current_user.is_authenticated:
                return redirect(url_for('index'))
            
            # استخدام النموذج الموجود...
            form = login.__globals__.get('LoginForm')()
            
            if form.validate_on_submit():
                user = User.query.filter_by(username=form.username.data).first()
                
                if user and check_password_hash(user.password_hash, form.password.data):
                    # تسجيل الدخول المستخدم
                    remember = form.remember.data if hasattr(form, 'remember') else False
                    login_user(user, remember=remember)
                    
                    # التحقق من وجود رابط التحويل
                    next_page = session.get('next')
                    if next_page:
                        session.pop('next', None)
                        return redirect(next_page)
                    
                    flash('تم تسجيل الدخول بنجاح!', 'success')
                    return redirect(url_for('index'))
                else:
                    flash('فشل تسجيل الدخول. يرجى التحقق من اسم المستخدم وكلمة المرور.', 'danger')
            
            # استخدام قالب العرض الموجود...
            return login.__globals__.get('render_template')('login.html', form=form)
        
        # استبدال الدالة الأصلية بالدالة المصححة
        import auth_routes
        auth_routes.login = fixed_login
        
        logger.info("تم إصلاح مسارات المصادقة بنجاح")
    except ImportError as e:
        logger.warning(f"لم يتم العثور على الوحدات المطلوبة لإصلاح مسارات المصادقة: {str(e)}")
    except Exception as e:
        logger.error(f"حدث خطأ أثناء إصلاح مسارات المصادقة: {str(e)}")
