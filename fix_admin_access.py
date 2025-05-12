
# إصلاح مشاكل وصول المسؤول إلى لوحة التحكم
import logging
import os
from flask import session, redirect, url_for, flash, request, g
from functools import wraps

logger = logging.getLogger(__name__)

def fix_admin_access():
    """إصلاح مشاكل وصول المسؤول"""
    try:
        from app import admin_required
        from models import User, UserRole
        from flask_login import current_user
        
        # تعديل المصحح (decorator) لفحص صلاحيات المسؤول بشكل صحيح
        def fixed_admin_required(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                if not current_user.is_authenticated:
                    flash('يرجى تسجيل الدخول أولاً للوصول إلى لوحة التحكم.', 'warning')
                    session['next'] = request.url
                    return redirect(url_for('login'))
                
                if not hasattr(current_user, 'role') or current_user.role != UserRole.ADMIN.value:
                    flash('لا تملك صلاحيات كافية للوصول إلى هذه الصفحة.', 'danger')
                    return redirect(url_for('index'))
                
                return f(*args, **kwargs)
            return decorated_function
        
        # استبدال الدالة الأصلية بالدالة المصححة
        import app
        app.admin_required = fixed_admin_required
        
        logger.info("تم إصلاح مشاكل وصول المسؤول بنجاح")
    except ImportError as e:
        logger.warning(f"لم يتم العثور على الوحدات المطلوبة لإصلاح وصول المسؤول: {str(e)}")
    except Exception as e:
        logger.error(f"حدث خطأ أثناء إصلاح وصول المسؤول: {str(e)}")
