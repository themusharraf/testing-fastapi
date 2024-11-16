# Api Unit va Integration test bilan qoplash

# 🚀 FastAPI Foydalanuvchilarni Boshqarish API

Ushbu **FastAPI** ilovasi foydalanuvchilarni boshqarish uchun mo‘ljallangan. Ilova **POST** va **GET** so‘rovlarini amalga oshiradi va ma’lumotlarni xotirada saqlaydi.

---

## 📋 Xususiyatlari

- **POST** so‘rovi orqali yangi foydalanuvchi qo‘shish.
- **GET** so‘rovi orqali foydalanuvchini ID bo‘yicha olish.
- Takroriy foydalanuvchini qo‘shishga yoki mavjud bo‘lmagan foydalanuvchini qidirishga oid xatoliklarni qayta ishlaydi.

---

## 🛠 O'rnatish

1. Zarur kutubxonalarni o'rnatish:
   ```bash
   pip install fastapi uvicorn pydantic
   ```
2. ▶️ Ilovani Ishga Tushirish
```bash
uvicorn main:app --reload
```
Odatiy holda server http://127.0.0.1:8000/docs manzilida ishga tushadi.

