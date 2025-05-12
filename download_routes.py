# Copyright حقوق النشر
# تمت إضافة روابط التنزيل

from flask import Blueprint, render_template_string, send_file
import os

download_bp = Blueprint('download', __name__)

@download_bp.route('/download_template')
def download_template():
    html = """
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تحميل قالب موقع المحفظة</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 20px;
                text-align: center;
                direction: rtl;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                margin-bottom: 30px;
            }
            p {
                color: #666;
                line-height: 1.6;
                margin-bottom: 20px;
                text-align: right;
            }
            .download-btn {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 12px 30px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                margin-top: 20px;
                transition: background-color 0.3s;
            }
            .download-btn:hover {
                background-color: #45a049;
            }
            .note {
                font-size: 0.9em;
                margin-top: 40px;
                color: #888;
            }
            .features {
                text-align: right;
                margin: 20px 0;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 5px;
            }
            .features h3 {
                margin-top: 0;
                color: #444;
            }
            .features ul {
                text-align: right;
                padding-right: 20px;
            }
            .features li {
                margin-bottom: 8px;
                list-style-type: disc;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>قالب موقع المحفظة الشخصية</h1>
            <p>هذا الملف يحتوي على جميع الملفات الأساسية اللازمة لتشغيل موقع المحفظة الشخصية على منصة Vercel.</p>
            
            <div class="features">
                <h3>محتويات الملف:</h3>
                <ul>
                    <li>جميع ملفات Python الأساسية</li>
                    <li>ملفات HTML و CSS و JavaScript</li>
                    <li>ملفات تكوين Vercel</li>
                    <li>ملف متطلبات Python</li>
                    <li>ملف إعدادات بيئة العمل النموذجي</li>
                </ul>
                
                <h3>ميزات الموقع:</h3>
                <ul>
                    <li>لوحة تحكم المسؤول الكاملة</li>
                    <li>معرض أعمال مع دعم التعليقات والإعجابات</li>
                    <li>نظام إحصائيات وتتبع الزوار</li>
                    <li>دعم التكامل مع Telegram وSendGrid</li>
                    <li>واجهة متعددة اللغات</li>
                    <li>معرض أعمال مشابه لإنستجرام</li>
                </ul>
            </div>
            
            <p>لتحميل ملف ZIP الذي يحتوي على قالب الموقع، انقر على الزر أدناه:</p>
            <a href="/download_file" class="download-btn">تحميل القالب</a>
            
            <div class="note">
                <p>ملاحظة: يجب إعداد قاعدة بيانات PostgreSQL واضافة المتغيرات البيئية المناسبة في Vercel.</p>
                <p>اقرأ ملف README.md المضمّن في الأرشيف للحصول على تعليمات الإعداد الكاملة.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@download_bp.route('/download_file')
def download_file():
    zip_file = os.path.join(os.getcwd(), 'clean_portfolio_template.zip')
    return send_file(zip_file, as_attachment=True, download_name='portfolio_template.zip')

@download_bp.route('/download/<filename>')
def download_custom_file(filename):
    """تنزيل ملف محدد من المجلد الجذر للمشروع"""
    if not os.path.exists(filename):
        return "الملف غير موجود", 404
    
    return send_file(filename, as_attachment=True, download_name=filename)

@download_bp.route('/render/download')
def render_download_page():
    """عرض صفحة تنزيل حزمة Render"""
    html = """
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تنزيل حزمة Render المحسنة</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 20px;
                text-align: center;
                direction: rtl;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                margin-bottom: 30px;
            }
            p {
                color: #666;
                line-height: 1.6;
                margin-bottom: 20px;
                text-align: right;
            }
            .download-btn {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 12px 30px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                margin-top: 20px;
                transition: background-color 0.3s;
            }
            .download-btn:hover {
                background-color: #45a049;
            }
            .note {
                font-size: 0.9em;
                margin-top: 40px;
                color: #888;
            }
            .features {
                text-align: right;
                margin: 20px 0;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 5px;
            }
            .features h3 {
                margin-top: 0;
                color: #444;
            }
            .features ul {
                text-align: right;
                padding-right: 20px;
            }
            .features li {
                margin-bottom: 8px;
                list-style-type: disc;
            }
            .fixes {
                background-color: #eaffea;
                padding: 15px;
                border-radius: 5px;
                border-right: 4px solid #4CAF50;
                margin: 20px 0;
            }
            .fixes h3 {
                color: #2e7d32;
                margin-top: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>حزمة النشر المحسنة على Render</h1>
            <p>هذا الملف يحتوي على جميع الملفات الأساسية اللازمة لتشغيل موقع المحفظة الشخصية على منصة Render.</p>
            
            <div class="fixes">
                <h3>✅ تم إصلاح المشكلات</h3>
                <ul>
                    <li>إصلاح مشكلة نموذج الطلب والأخطاء التي تظهر عند الإرسال</li>
                    <li>إصلاح مشكلة خطأ 500 في لوحة التحكم</li>
                    <li>تحسين التحقق من صلاحيات المستخدمين في واجهات الإدارة</li>
                    <li>إصلاح إشعارات تيليجرام لمنع حدوث أخطاء ظاهرة للمستخدم</li>
                </ul>
            </div>
            
            <div class="features">
                <h3>محتويات الحزمة:</h3>
                <ul>
                    <li>جميع ملفات Python الأساسية</li>
                    <li>ملفات HTML و CSS و JavaScript</li>
                    <li>ملفات تكوين Render</li>
                    <li>ملف متطلبات Python</li>
                    <li>مجلدات فارغة للصور والوسائط</li>
                </ul>
                
                <h3>مميزات:</h3>
                <ul>
                    <li>حجم مضغوط أقل من 1 ميغابايت (617 كيلوبايت)</li>
                    <li>جاهز للنشر مباشرة على Render</li>
                    <li>بدون ملفات وسائط - يمكنك رفعها لاحقاً</li>
                    <li>يعمل بنفس الشكل تماماً كما في البريفيو</li>
                    <li>بنية ملفات احترافية ومرتبة</li>
                </ul>
            </div>
            
            <p>لتحميل ملف ZIP المحسن الذي يحتوي على حزمة النشر، انقر على الزر أدناه:</p>
            <a href="/download/improved" class="download-btn">تحميل الحزمة المحسنة</a>
            
            <div class="note">
                <p>ملاحظة: يجب إعداد قاعدة بيانات PostgreSQL وإضافة المتغيرات البيئية المناسبة في Render.</p>
                <p>اقرأ ملف README.md المضمّن في الأرشيف للحصول على تعليمات الإعداد الكاملة.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@download_bp.route('/download/render')
def download_render_package():
    """تنزيل حزمة الموقع جاهزة للنشر على Render"""
    zip_file = os.path.join(os.getcwd(), 'render_deployment_package.zip')
    
    if not os.path.exists(zip_file):
        return "ملف حزمة Render غير موجود. يرجى إنشاؤه أولاً.", 404
    
    return send_file(zip_file, as_attachment=True, download_name='render_deployment_package.zip')
