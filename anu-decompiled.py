from py_compile import compile as c
import subprocess as sp, os, sys
h = '\x1b[92m'
m = '\x1b[91m'
x = '\x1b[0m'
try:
    import uncompyle6
except ModuleNotFoundError:
    sp.call('pip install uncompyle6', shell=True, stdout=(sp.DEVNULL), stderr=(sp.STDOUT))

def pejuang_ldr():
    os.system('clear')
    print(h + u'\n\u28b8\u28d7\u287f\u28b8\u287fP\u2877\u28cf\u286f\u28df\u28f7Y\u2867\u28d7\u28ef\u28ff\u28df\u28c7T\u28ef\u28f7\u285f\u285f\u28b8\u2857H\u28d7\u2857\u28cf\u2857\u2877\u28d7O\u28ef\u287f\u28e7N\u2857\u284f\u287f\u284f\u28b8\u28cf\u28ef\n\u287f\u28d7\u28e7C\u2867\u28dfO\u284f\u28ff\u285fM\u28cf\u2847\u287f\u2867\u285f\u284fP\u28e7\u2857\u2867Y\u2877\u28d7L\u28c7\u285f\u284f\u285fE\u28ff\u287f\u287fR\u286f\u28ef\u287f\u2857\u284f\u287f\u284f\u28b8\u28cf\u28ef\n\u2867\u28df\u284f\u28ef\u286f\u287f\u28ef\u28ff\u2867\u2847\u2877\u2877\u287f\u28c7\u2857\u284f\u287f\u284f\u28b8\u28cf\u28ef\u28df\u2857\u28b8\u284f\u286f\u2877\u28b8\u2857\u2877\u2867\u28d7\u28ff\u28b8\u28ef\u2847\u2857\u28c7\u287f\u286f\u2857\u284f\u287f\u284f\n\u28df\u287f\u28ef\u28f7\u2847\u286f\u28c7\u286f\u2877K\u28ff\u28cf\u28e7\u2847a\u28d7\u2867r\u28df\u284f\u28ff\u28f7\u28e7\u28dfj\u285f\u28b8\u28b8\u28b8\u2867\u2847\u28f7o\u28e7\u28c7\u28c7\u287f\u2847k\u2877\u2867\u28e7\u2877\u28f7\n\u284f\u2847\u2857\u28f7\u284f\u28df\u2877\u2857\u2877\u2867\u28b8\u2857\u284f\u287f\u2867\u2857CRABS_ID\u2857\u287f\u284f\u28ef\u284f\u284f\u2867\u28df\u285f\u28b8\u28cf\u2877\u28e7\u2867\u286f\u2847\u28cf\u284f\u2857\u284f\n ' + m + 'h t t p s : / / t . m e / C R A B S _ I D\n')
    print(x + '1.' + h + ' Compyler')
    print(x + '2.' + h + ' Uncompyler')
    print(x + '0.' + h + ' Minggat')
    ops = input(h + '\nMau ngapain gayn ? : ' + x)
    while ops != '1':
        if ops != '2':
            if ops != '0':
                print(m + 'emmuach ! :* ')
                ops = input(h + 'Mau ngapain gayn ? : ' + x)

    if ops == '1':
        karjok()
    elif ops == '2':
        pangesty()
    else:
        print(m + 'Oke, lu burrique, gw gans. tq' + x)
        sys.exit()


def karjok():
    z = input(h + '\nNama file: ' + x)
    nf = z.split('.')[0]
    if z == '':
        sys.exit()
    else:
        try:
            c(z)
        except ValueError:
            print(m + 'nullbyte')
            sys.exit()

        try:
            os.system('cd __pycache__ && mv ' + nf + '.cpython-37.pyc ' + nf + '_terkompile.py')
            os.system('cd __pycache__ && mv ' + nf + '_terkompile.py ..')
            print(h + 'oke gayn.. sukses !')
            print(h + 'hasilnya ' + x + nf + '_terkompile.py')
            print(m + '+++++++++++++++++++++++++++++++++++++++++++')
            ask = input(m + 'lagi ? y/n: ' + x)
            if ask == 'y':
                karjok()
            else:
                pejuang_ldr()
        except Exception as se:
            try:
                print(se)
                ask = input(h + 'lagi ? y/n: ' + x)
                if ask == 'y':
                    karjok()
                else:
                    pejuang_ldr()
            finally:
                se = None
                del se


def pangesty():
    z = input(h + '\nNama file: ' + x)
    nf = z.split('.')[0]
    if 'sytd.py' in z or 'anu.py' in z:
        os.system('clear')
        tny = input(m + 'Anda mencoba menguncompyle file terkontaminasi virus.\nyakin ingin lanjut ?\n(mungkin file system akan terhapus) y/n: ' + x)
        if tny == 'y':
            while True:
                print(m + u'\u28b8\u28d7\u287f\u28b8\u287fP\u2877\u28cf\u286f\u28df\u28f7Y\u2867\u28d7\u28ef\u28ff\u28df\u28c7T\u28ef\u28f7\u285f\u285f\u28b8\u2857H\u28d7\u2857\u28cf\u2857\u2877\u28d7O\u28ef\u287f\u28e7N\u2857\u284f\u287f\u284f\u28b8\u28cf\u28ef\u287f\u28d7\u28e7C\u2867\u28dfO\u284f\u28ff\u285fM\u28cf\u2847\u287f\u2867\u285f\u284fP\u28e7\u2857\u2867Y\u2877\u28d7L\u28c7\u285f\u284f\u285fE\u28ff\u287f\u287fR\u286f\u28ef\u287f\u2857\u284f\u287f\u284f\u28b8\u28cf\u28ef\u2867\u28df\u284f\u28ef\u286f\u287f\u28ef\u28ff\u2867\u2847\u2877\u2877\u287f\u28c7\u2857\u284f\u287f\u284f\u28b8\u28cf\u28ef\u28df\u2857\u28b8\u284f\u286f\u2877\u28b8\u2857\u2877\u2867\u28d7\u28ff\u28b8\u28ef\u2847\u2857\u28c7\u287f\u286f\u2857\u284f\u287f\u284f\u28df\u287f\u28ef\u28f7\u2847\u286f\u28c7\u286f\u2877K\u28ff\u28cf\u28e7\u2847a\u28d7\u2867r\u28df\u284f\u28ff\u28f7\u28e7\u28dfj\u285f\u28b8\u28b8\u28b8\u2867\u2847\u28f7o\u28e7\u28c7\u28c7\u287f\u2847k\u2877\u2867\u28e7\u2877\u28f7\u284f\u2847\u2857\u28f7\u284f\u28df\u2877\u2857\u2877\u2867\u28b8\u2857\u284f\u287f\u2867\u2857CRABS_ID\u2857\u287f\u284f\u28ef\u284f\u284f\u2867\u28df\u285f\u28b8\u28cf\u2877\u28e7\u2867\u286f\u2847\u28cf\u284f\u2857\u284fh t t p s : / / t . m e / C R A B S _ I D')

        else:
            sys.exit()
    elif z == '':
        sys.exit()
    else:
        try:
            os.mkdir('__pycache__')
        except OSError:
            pass

        os.system('cp ' + z + ' __pycache__')
        os.system('cd __pycache__ && mv ' + z + ' ' + nf + '.cpython-37.pyc')
        fl = 'uncompyle6 ' + z
        with open(nf + '_terUncompile.py', 'w') as (o):
            sp.call(fl, shell=True, stdout=o)
        print(h + 'mantab gayn.. unkompil sukses !')
        print(h + 'hasilnya ' + x + nf + '_terUncompile.py')
        print(m + '+++++++++++++++++++++++++++++++++++++++++++')
        o.close()
        ask = input(m + 'lagi ? y/n: ' + x)
        if ask == 'y':
            pangesty()
        else:
            os.system('cd __pycache__ && rm ' + nf + '.cpython-37.pyc')
            pejuang_ldr()


if __name__ == '__main__':
    pejuang_ldr()
