# کانفیگ‌یار

پروژه Flask فارسی و RTL با 56 کانفیگ VLESS و دکمه «کپی همه کانفیگ‌ها».

## اجرا
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```
سپس: http://127.0.0.1:5000

## Deploexo / Docker
Start command: `gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 "app:create_app()"`

کانفیگ‌ها در `content/configs/configs.json` هستند.
