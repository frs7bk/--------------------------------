"""
وظائف التحكم في الوصول والأمان
تتضمن وظائف التحقق من صلاحيات المستخدم وقيود الوصول
"""

from functools import wraps
from flask import redirect, url_for, flash, session, request
from flask_login import current_user

def admin_required(f):
    """
    مزخرف للتحقق من أن المستخدم الحالي هو مسؤول
    يستخدم للتحكم في الوصول إلى صفحات الإدارة
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('يجب تسجيل الدخول للوصول إلى هذه الصفحة', 'error')
            return redirect(url_for('admin_login', next=request.url))
        
        if not current_user.role == 'admin':
            flash('لا تملك صلاحيات كافية للوصول إلى هذه الصفحة', 'error')
            return redirect(url_for('index'))
            
        return f(*args, **kwargs)
    return decorated_function

def api_admin_required(f):
    """
    مزخرف للتحقق من أن المستخدم الحالي هو مسؤول، مناسب للواجهات البرمجية
    يرجع استجابة JSON بدلاً من إعادة التوجيه
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.role == 'admin':
            return {'error': 'غير مصرح'}, 403
        return f(*args, **kwargs)
    return decorated_function

def user_required(f):
    """
    مزخرف للتحقق من أن المستخدم مسجل الدخول
    يستخدم للتحكم في الوصول إلى صفحات المستخدم
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('يجب تسجيل الدخول للوصول إلى هذه الصفحة', 'error')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function