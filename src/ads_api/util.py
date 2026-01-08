def to_camel(string: str) -> str:
    """将字符串转为驼峰"""
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])
