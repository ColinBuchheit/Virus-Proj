# this file is infected
print("This file is infected")
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNoDAAAAAAE=')))")


def main():
    print("This is a test program.")

if __name__ == "__main__":
    main()

