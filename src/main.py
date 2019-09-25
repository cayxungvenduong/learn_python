import xml2csv

if __name__ == '__main__':
    try:
        xml2csv.Xml2Csv().train()
        print('OK')
    except Exception as ex:
        print(ex)
