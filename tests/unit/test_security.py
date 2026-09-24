from app.core.security import hash_password, verify_password


def test_password_hash_can_be_verified():
    password = "MySecurePassword123"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True


def test_wrong_password_fails_verification():
    password = "MySecurePassword123"
    wrong_password = "WrongPassword123"

    hashed_password = hash_password(password)

    assert verify_password(wrong_password, hashed_password) is False