from typing import Dict

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class InvaildMessageType(TypeError):
    pass


def rotate_string(msg: str, shift: int) -> str:
    return msg[shift:] + msg[:shift]


def create_shifted_alphabet(shift: int) -> Dict[str, str]:
    """Given a shift return a dictionary with the
    shifted alphabath

    Example
    -------
    >> new_letters = create_shifted_alphabet(shift=1)
    >> print(new_letters)
    new_letters = {"a": "b", "b": "c", ...}

    Parameters
    ----------
    shift : int
        The number of places to shift the alphabet

    Returns
    -------
    Dict[str, str]
        Dictionary with the original alphabet as keys and
        the new letters as values
    """

    new_letters = {}
    rotated_alphabet = rotate_string(ALPHABET, shift=shift)

    for letter, new_letter in zip(ALPHABET, rotated_alphabet):
        new_letters[letter] = new_letter

    return new_letters


def encrypt(message: str, shift: int) -> str:
    """Encrypt message with caesar shift

    Parameters
    ----------
    message : str
        The message you want to encrypt
    shift : int
        The cesar shift used to encrypt the message

    Returns
    -------
    str
        The encrypted message
    """

    if not isinstance(message, str):
        raise InvaildMessageType(
            f"Invalid message of type {type(message)}, expected str"
        )

    new_letters = create_shifted_alphabet(shift=shift)

    encrypted_message = ""
    for letter in message.lower():
        encrypted_message += new_letters[letter]

    return encrypted_message


def decrypt(encrypted_message: str, shift: int) -> str:
    """Decrypt the encypted message using ceaser shift

    Parameters
    ----------
    encrypted_message : str
        The message that should be decrypted
    shift : int
        The ceasr shift

    Returns
    -------
    str
        Deacrypted message
    """
    return encrypt(encrypted_message.lower(), -shift)
