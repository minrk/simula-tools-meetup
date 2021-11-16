# https://cryptii.com/pipes/caesar-cipher

import pytest
import caesar_cipher


@pytest.mark.parametrize(
    "msg, shift, expected_output", [("hello", 1, "ifmmp"), ("welcome", 7, "dlsjvtl")]
)
def test_encrypt(msg, shift, expected_output):
    assert caesar_cipher.encrypt(msg, shift=shift) == expected_output


@pytest.mark.parametrize(
    "encrypted_msg, shift, expected_output",
    [("ifmmp", 1, "hello"), ("dlsjvtl", 7, "welcome")],
)
def test_decrypt(encrypted_msg, shift, expected_output):
    assert caesar_cipher.decrypt(encrypted_msg, shift=shift) == expected_output


@pytest.mark.parametrize(
    "msg, shift",
    [
        ("programming", 3),
        ("math", 15),
        ("physics", -18),
        ("Hei", 6),
    ],
)
def test_encrypt_decrypt_yields_same_result(msg, shift):
    encrypted_message = caesar_cipher.encrypt(message=msg, shift=shift)
    decrypted_message = caesar_cipher.decrypt(
        encrypted_message=encrypted_message, shift=shift
    )
    assert decrypted_message == msg.lower()


def test_encrypt_raises_TypeError_on_int_input():
    with pytest.raises(TypeError):
        caesar_cipher.encrypt(1910, 4)


@pytest.mark.parametrize(
    "letter, new_letter, shift",
    [
        ("a", "b", 1),
        ("m", "n", 1),
        ("z", "a", 1),
        ("a", "f", 5),
        ("m", "r", 5),
        ("z", "e", 5),
        ("a", "a", 26),
        ("m", "m", 26),
        ("z", "z", 26),
    ],
)
def test_create_shifted_alphabet(letter, new_letter, shift):
    new_letters = caesar_cipher.create_shifted_alphabet(shift)
    assert new_letters[letter] == new_letter


def test_rotate_string():
    assert caesar_cipher.rotate_string("hello", 1) == "elloh"
    assert caesar_cipher.rotate_string("hello", 2) == "llohe"
