import gspread
credentials = {
        "type": "service_account",
        "project_id": "manifest-virtue-353609",
        "private_key_id": "33bcba435fe45f0c05a50bfdcf897f93c2539226",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC7gjdycedEdqCQ\nSapamuI1ZgLlPQZoSOGKCdx6GyvwhuoHrnjFcm0t64iHqkrPW4eA7brDR/ZYRaSl\n6HYc7gnULX87/yXCdI1kGNSDOccCKjUbCBthLiInMi/J+XFk81UknLlUj08qQSMT\n7jvLfvHQlaTDynOMRPMKk3Yx7LbqKZvedjTdB52wPx0i0qTL7ZxFQBwB62ipkA7h\nFCFgho0r4LZC8BC4OXpgMqt8NrIWNVJ+JfT9DY5ZdjXsPO496wSCV0jT3BFKUW37\nC+Gl36xosSofuUo+qRabG5nw6uzfouZSLJ6U+ElUf6jjyo/3yZvX7p7vsV7O2JHG\nQXN1eo9FAgMBAAECggEABbgoFs6Qnk78AMqubosQ4U4WQoXE/0NR1dMNLZBMm86R\nruBMgMFHwUHQ7Uptc7u3+1/E9ZXpVrHxHrpjd+hu1lD484yJy0+gzG/Rc5s8jb1Z\n11Q8+Y7drdJjEMcSBWFCtJYvNPwWDxTjjAUVP9TEbXdTCkHPmnSz8RukXEt7HNNQ\nnRydMNDXMZYzHfhW+9SSvWNuJxFbRHsfYhpuaqeI3CjVqMJbeBCa7VnwetOmO/8W\nMp+kSnTZ9zSBb8+YHLbRFjVELg0nk/nlUzgtkBJAnUa2TL1OTQhoWGYgtaYYw4QF\n0vzRU6JxvH27B7oD6KxkX/frHPNWYyfaxHMrYjGmwQKBgQD32ncNroEAxa0Z8ArO\ns6KmEx6acC5eohzsVl4CjQLyzRq4TCTElnzssKDJN+2wkTocahfUdu1P3f92b84C\nv2r/HLzE1CRgB28YyA6dh+gXxzSwJswxwje5VN3A019j6ZMY6krgs9XwqY/dmjAK\nekOBzsUVg04WroYydZqr94vWdQKBgQDBq/zPJY6uBatoOBnNnvHiWc8Xd+6vYW3G\nDPntgrZAH84VUt674KumaGIjOaOq3Y98CdSjIvx1zHfRgKfKSTwLaagKbOnQG6LG\nQ9RQQE/bYey3AEa8PJOCT0YHwmNl69gNDWLrBzLRsk37glSEYKu/EGyhxbgEUTYU\nfJXlaZDbkQKBgQC8mFO26W3n9IK/FdRjbHT7Adlrkqj2AU0Y2K84KaxwrHkEe4wO\nuqPcRppSAmiuzhL1xBTV6pixCS92I6USmi0Eag2JiBMVrxJuPOxCGkQUs9P3pc4C\nntJgB5+lNjGDiRwQ/VZ0nOLR+XQrH0Qm9NmhUIDO2db1k18xziMfb4HMcQKBgQCG\n1nNA1WktB417FfQBELRfXx+ruzhWqoJ+7PHkxqiUpJAakIO6UoWvaeVJmQu2HmOT\nfFSq7+TNLvoMxoILeElxuLHh8EopNdRyLS9YYC45E0h3cJ3O2G3qv76GEHSbtUPK\ncpN4Bp7/GCDrBqZJM/TfJVQ8nSes+c2pHcRO4NyVwQKBgAkrMIMpbcHcrhlmhfbi\nDjn3lmBkZFE+W0OUeybkr2NZt8GzSSuTxX2oNozciBc0Y+S+SchDUL/vQvI+mDrs\n2GcsEXBe2AveKFhJH0eskKoYB7pqZZxxbm2fWW++BBrCexKh+hgRRiGr6w8Jt4mN\njbyoXdxFTVgNwgEDSQUPVkr/\n-----END PRIVATE KEY-----\n",
        "client_email": "service-account@manifest-virtue-353609.iam.gserviceaccount.com",
        "client_id": "113640244737897099808",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-account%40manifest-virtue-353609.iam.gserviceaccount.com"
        }

gc = gspread.service_account_from_dict(credentials)

worksheet = gc.open_by_key("13EJk4vZTSTzITEoEW2SivSySV0eKe8Sw09m51eOI9qk")

current_sheet=worksheet.worksheet("Sheet1")

print(current_sheet.get_all_values())
