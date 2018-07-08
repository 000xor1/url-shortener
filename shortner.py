import os
import sys

# init
BASE62 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE62_NUM = 62

HOME = "http://tmu.kr/"

DATABASE_1 = {}
DATABASE_2 = {}


def long2short(idx, base62=BASE62):

    arr = []

    if idx  == 0:
        arr.append(base62[0])

    else:
        while idx:
            idx, rem = divmod(idx, BASE62_NUM)
            arr.append(base62[rem])
        arr.reverse()

    return arr[0]


def short2long(url):

    if url in DATABASE_2:
        result = DATABASE_2[url]

    else:
        result = "Not Found"

    return result


def main():

    longUrls = ["http://000xor1.github.com",
                "http://twitter.com/000xor1",
                "http://kakao.com",
                "http://naver.com",
                "http://neftlix.com"
                ]

    shortUrls = []

    print("\n")

    # long to short
    for url in longUrls:
        db_length = len(DATABASE_1)
        DATABASE_1[db_length] = url


        shorturl = long2short(db_length,BASE62)
        DATABASE_2[shorturl] = url

        shortUrls.append(shorturl)

        print("Long to short: [ {} ] -> [ {} ]".format(url, HOME+shorturl))

    print("\n")

    #short to long (redirection)
    for url in shortUrls:
        longUrl = short2long(url)

        print("Short to Long : [ {} ] -> [ {} ]".format(HOME+url, longUrl))

    print("\n")


if __name__ == "__main__":
    main()
