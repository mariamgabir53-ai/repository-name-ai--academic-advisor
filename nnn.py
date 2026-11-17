import streamlit as st

st.set_page_config(
    page_title="نظام الإرشاد الأكاديمي الخبير", page_icon="🎓"
)

# تحسين اتجاه النصوص العربية (RTL)
st.markdown(
    """
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎓 نظام الإرشاد الأكاديمي الخبير - قسم الذكاء الاصطناعي")
st.write(
    "أدخل بياناتك أدناه لمعرفة الحد الأقصى للساعات، المواد المرشحة للتسجيل، ومصادر التعلم أونلاين:"
)

# إدخال بيانات الطالب
name = st.text_input("اسم الطالب:")
gpa = st.number_input(
    "المعدل التراكمي (GPA):", min_value=0.0, max_value=4.0, value=3.0, step=0.01
)

st.subheader("المواد التي تم اجتيازها بنجاح:")
col1, col2 = st.columns(2)

with col1:
    passed_python = st.checkbox("برمجة بايثون (Python Programming)")
    passed_math = st.checkbox("جبر خطي ومصفوفات (Linear Algebra)")
    passed_db = st.checkbox("قواعد بيانات (Database Basics)")

with col2:
    passed_ml = st.checkbox("تعلم الآلة (Machine Learning)")
    passed_img = st.checkbox("معالجة الصور (Image Processing)")

# جمع المواد المجتازة
completed = []
if passed_python:
    completed.append("Python Programming")
if passed_math:
    completed.append("Linear Algebra")
if passed_db:
    completed.append("Database Basics")
if passed_ml:
    completed.append("Machine Learning")
if passed_img:
    completed.append("Image Processing")

# زر التحليل
if st.button("🔍 تحليل الحالة وإصدار التوصيات"):
    if not name.strip():
        st.warning("يرجى إدخال اسم الطالب أولاً.")
    else:
        # محرك الاستدلال للحالة الأكاديمية
        if gpa >= 3.0:
            max_credits = 18
            academic_status = "ممتاز / أداء عالي (High Standing)"
            advice = "يمكنك تسجيل حتى 18 ساعة معتمدة والتسجيل في مشاريع تقدمية."
        elif gpa >= 2.0:
            max_credits = 15
            academic_status = "منتظم / حالة طبيعية (Good Standing)"
            advice = "العبء الموصى به هو 15 ساعة معتمدة للتركيز والتحصيل."
        else:
            max_credits = 12
            academic_status = "⚠️ إنذار أكاديمي (Academic Probation)"
            advice = "يجب التركيز على رفع المعدل وإعادة المواد ذات التقدير المنخفض."

        # محرك الاستدلال للمواد المقترحة مع مصادرها
        recommended_courses = []

        if "Machine Learning" in completed:
            recommended_courses.append({
                "name": "Deep Learning (التعلم العميق)",
                "resource": "كورس Deep Learning Specialization (Andrew Ng - Coursera)"
            })
        elif "Python Programming" in completed and "Linear Algebra" in completed:
            recommended_courses.append({
                "name": "Machine Learning (تعلم الآلة)",
                "resource": "كورس Machine Learning Specialization (Andrew Ng)"
            })
        else:
            if "Python Programming" not in completed:
                recommended_courses.append({
                    "name": "Python Programming (متطلب أساسي)",
                    "resource": "كورس Python for Everybody (Dr. Chuck - Coursera/YouTube)"
                })
            if "Linear Algebra" not in completed:
                recommended_courses.append({
                    "name": "Linear Algebra (متطلب أساسي)",
                    "resource": "سلاسل شرح Linear Algebra (3Blue1Brown - YouTube)"
                })

        if "Database Basics" in completed:
            recommended_courses.append({
                "name": "Data Engineering & Big Data (هندسة البيانات)",
                "resource": "كورسات Introduction to Data Engineering (Coursera)"
            })
        else:
            recommended_courses.append({
                "name": "Database Basics (قواعد بيانات)",
                "resource": "كورس SQL for Data Analysis (Coursera / YouTube)"
            })

        if "Image Processing" in completed:
            recommended_courses.append({
                "name": "Computer Vision (رؤية الحاسوب)",
                "resource": "مقدمة في Computer Vision (OpenCV / PyImageSearch)"
            })
        elif "Python Programming" in completed:
            recommended_courses.append({
                "name": "Image Processing (معالجة الصور)",
                "resource": "مكتبات Pillow و OpenCV (YouTube tutorials)"
            })

        # عرض النتائج
        st.divider()
        st.success(f"تم تحليل بيانات الطالب: {name}")

        st.markdown("### 📋 تقرير الإرشاد الأكاديمي")
        st.write(f"**المعدل التراكمي:** {gpa:.2f}")
        st.write(f"**الحالة الأكاديمية:** {academic_status}")
        st.write(f"**الحد الأقصى للساعات المسموحة:** {max_credits} ساعة")

        st.info(f"💡 **نصيحة إرشادية:** {advice}")

        st.markdown("#### 📚 المواد المقترحة ومصادر التعلم أونلاين:")
        
        report_text = f"""--- تقرير الإرشاد الأكاديمي ---
اسم الطالب: {name}
المعدل التراكمي: {gpa:.2f}
الحالة الأكاديمية: {academic_status}
الحد الأقصى للساعات: {max_credits} ساعة
النصيحة: {advice}

المواد المقترحة ومصادرها:
"""

        if recommended_courses:
            for c in recommended_courses:
                st.markdown(f"- **{c['name']}**  \n  📌 *مصدر مقترح أونلاين:* {c['resource']}")
                report_text += f"- {c['name']} | المصدر المقترح: {c['resource']}\n"
        else:
            st.write("لا توجد مواد مقترحة حالياً، يرجى مراجعة المرشد الأكاديمي.")
            report_text += "لا توجد مواد مقترحة حالياً.\n"

        # زر تحميل التقرير كملف نصي (TXT)
        st.download_button(
            label="📥 تحميل التقرير وخطة الدراسة كملف (TXT)",
            data=report_text,
            file_name=f"Academic_Guidance_{name}.txt",
            mime="text/plain"
        )