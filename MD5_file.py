
import sys
import hashlib

def get_file_md5(fname):
    m = hashlib.md5()   #creat md5 file
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()
def get_file_sha256(filname):
    m=hashlib.sha256()
    with open(filname, "rb") as f:
        sha256obj = hashlib.sha256()
        sha256obj.update(f.read())
        hash_value = sha256obj.hexdigest()
        return hash_value


# reload(sys)
# sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    # file_name = r"D:\tool\BurpSuite v2.1\burp_suite_pro_v2020.12\burpsuite_pro_v2020.12.jar"
    file_name = r"E:\CentOS-7-x86_64-DVD-2003.iso"
    # file_name = r"F:\CentOS-7-x86_64-DVD-2003.iso"
    file_md5 = get_file_md5(file_name)
    file_sha256 = get_file_sha256(file_name)
    print(file_md5)     
    print(file_sha256)    