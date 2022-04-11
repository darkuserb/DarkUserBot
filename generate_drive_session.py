from pydrive.auth import GoogleAuth


def main():
    gauth = GoogleAuth()
    # Yaddaşda olan istəmci kimlik məlumatlarını qeyd et
    gauth.LoadCredentialsFile("secret.json")
    if gauth.credentials is None:
        # Orada deyillərsə kimlik doğrulaması et.
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Süresi dolubsa yenilə
        gauth.Refresh()
    else:
        # Qeyd edilən məlumatları başlat
        gauth.Authorize()
    # hazırkı kimlik məlumatlarını bir yerə qeyd et
    gauth.SaveCredentialsFile("secret.json")


if __name__ == '__main__':
    main()
