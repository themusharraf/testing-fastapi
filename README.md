# 🚀 FastAPI Foydalanuvchi Boshqaruvi API - Unit va Integration Testlar

Ushbu loyiha **FastAPI** asosida foydalanuvchilarni boshqarish API uchun mo'ljallangan. Loyiha ichida foydalanuvchilarni qo'shish va olish funksiyalari mavjud bo'lib, ularga **Unit test** va **Integration testlar** orqali sinovlar yozilgan.

---

## 📋 Xususiyatlar

- **Foydalanuvchi qo'shish** (POST so'rovi)
- **Foydalanuvchini olish** (GET so'rovi)
- **Unit testlar**: Foydalanuvchi yaratish va olishning asosiy logikasini izolyatsiyalangan holda sinash.
- **Integration testlar**: API endpointlarining to'g'ri ishlashini sinash.

---

## 🛠 O'rnatish

1. Zarur kutubxonalarni o'rnatish:
   ```bash
   pip install fastapi uvicorn pydantic pytest
   ```
2. ▶️ Ilovani Ishga Tushirish
   ```bash
   uvicorn main:app --reload
   ```
   Odatiy holda server http://127.0.0.1:8000/docs manzilida ishga tushadi.

3. 🔧 Testlarni Ishga Tushirish
   Testlarni ishga tushirish uchun quyidagilarni bajaring:
   Unit va Integration testlarni bajarish:
   ```bash
      pytest
   ```
Test natijalarini ko'rib chiqing. Hammasi muvaffaqiyatli o'tishi kerak.

## 🧪 Testlar Tafsiloti

### Integration Testlar
Integration testlar API endpointlarning ishlashini sinaydi. Quyidagi kod test_create_user_and_get funksiyasida API endpointlar orqali foydalanuvchini yaratish va olishni sinovdan o'tkazadi:
```python
def test_create_user_and_get():
    # Yangi foydalanuvchi qo'shish
    resp = client.post('/user/', json={"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"})
    assert resp.status_code == 200
    assert resp.json() == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # Foydalanuvchini olish
    resp = client.get('/user/4')
    assert resp.status_code == 200
    assert resp.json() == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # Takroran bir xil foydalanuvchini qo'shishga urinish
    resp = client.post('/user/', json={"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"})
    assert resp.status_code == 400
    assert resp.json() == {"detail": "User already exists"}

    # Mavjud bo'lmagan foydalanuvchini olish
    resp = client.get('/user/5')
    assert resp.status_code == 404
    assert resp.json() == {"detail": "User not found"}
```
### Unit Testlar
Unit testlar kodning logikasini izolyatsiyalangan holda sinash uchun yozilgan. Quyidagi testlar foydalanuvchini yaratish (create_user) va olish (get_user) funksiyalarini sinaydi.
Foydalanuvchi yaratish testi
```python
def test_create_user():
    # Yangi foydalanuvchi qo'shish
    user = create_user(4, "Bekzod", "bekzod", "bekzod@gmail.com")
    assert user == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}
    assert users[4] == user

    # Takroriy foydalanuvchini qo'shishga urinish
    with pytest.raises(ValueError, match="User already exists"):
        create_user(4, "Bekzod", "bekzod", "bekzod@gmail.com")
```
Foydalanuvchini olish testi
```python
def test_get_user():
    # Test uchun foydalanuvchi qo'shish
    users[4] = {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # Foydalanuvchini olish
    user = get_user(4)
    assert user == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # Mavjud bo'lmagan foydalanuvchini olishga urinish
    with pytest.raises(ValueError, match="User not found"):
        get_user(5)
```
## 📚 Qo‘shimcha Ma'lumotlar
- FastAPI hujjatlari: https://fastapi.tiangolo.com/
- Pytest hujjatlari: https://docs.pytest.org/
- Pydantic hujjatlari: https://pydantic-docs.helpmanual.io/

## 🌟 Hissa Qo‘shish
Loyihani fork qilib, yaxshilanishlar kiriting va pull request yuboring. Sizning hissangiz qadrlanadi! 😊



