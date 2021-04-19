def longestPalindrome(s: str) -> str:
    polindrom_str = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if len(substr)>len(polindrom_str):
                if str(substr[::-1])==str(substr):
                    polindrom_str = substr

    return polindrom_str


print(longestPalindrome('aesdffdsadfd'))
