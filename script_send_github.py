import os
import subprocess
import time

# إعدادات المستودع
REPO_DIR = os.path.dirname(os.path.abspath(__file__))  # ضع مسار مستودعك هنا
FILENAME = "test_file.txt"
COMMIT_MESSAGE = "Automated commit"
BRANCH = "main"

def run_command(command, cwd=None):
    """ تشغيل الأوامر وإرجاع النتيجة """
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

def git_add_commit_push(message):
    """ إضافة الملفات إلى Git، تنفيذ commit و push """
    run_command(f"git add .", cwd=REPO_DIR)
    run_command(f'git commit -m "{message}"', cwd=REPO_DIR)
    run_command(f"git push origin {BRANCH}", cwd=REPO_DIR)
num = int(input("Enter Your Number: "))
for i in range(num):
    print(f"--- Iteration {i+1} ---")

    # إنشاء الملف
    file_path = os.path.join(REPO_DIR, FILENAME)
    with open(file_path, "w") as f:
        f.write(f"This is test iteration {i+1}\n")

    # رفع التغييرات
    git_add_commit_push(f"{COMMIT_MESSAGE} - Added {FILENAME} (Iteration {i+1})")

    # انتظار قليلًا لضمان استقرار العمليات
    time.sleep(2)

    # حذف الملف
    os.remove(file_path)

    # رفع التغييرات بعد الحذف
    git_add_commit_push(f"{COMMIT_MESSAGE} - Removed {FILENAME} (Iteration {i+1})")

    time.sleep(2)

print("تمت العملية بنجاح!")
