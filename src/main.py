from pikepdf import Pdf as ppdf
import pikepdf
import warnings
import asyncio

# with ppdf.open('test/rsc/a.pdf') as doc:
#     pass

# try:
#     with ppdf.open('test/rsc/ab.pdf') as doc:
#         pass
# except FileNotFoundError:
#     print('file not found')


# try:
#     with ppdf.open('test/rsc/non-pdf.pdf') as doc:
#         pass
# except pikepdf.PdfError:
#     print('pdferror')


# with ppdf.open('test/rsc/encrypted.pdf', password='password') as doc:
#     pass

# with warnings.catch_warnings():
# warnings.simplefilter("ignore")
# with ppdf.open('test/rsc/a.pdf', password='pass') as doc:
#     print(doc.is_encrypted)

# try:
#     with ppdf.open('test/rsc/encrypted.pdf', password='pass') as doc:
#         pass
# except pikepdf.PasswordError:
#     print('password error')


# with pikepdf.open('test/rsc/a.pdf') as doc:
#     password = 'password'
#     e = pikepdf.Encryption(owner='', user='')
#     doc.save('test/rsc/a_encrypted.pdf', encryption=e)


# async def echo():
#     print('readed')


# async def savetask(doc):
#     doc.save('../encrypted_decrypt.pdf')


# async def decryption():
#     with pikepdf.open('../encrypted.pdf', password='Hirata+2021') as doc:
#         task1 = asyncio.create_task(echo())
#         task2 = asyncio.create_task(savetask(doc))

#         await task1
#         await task2

#         print('saved')


# print('start')
# asyncio.run(decryption())

from functools import reduce

A = [(1, 3), (5, 6), (7, 'end'), (10, 13), (20, 21)]

F = reduce(lambda x, y: list(x)+list(y), A)

if F.count('end') == 1 and F.index('end') == len(F)-1:
    print(F.index('end'))

if F.count('end') > 1 or F.index('end') != len(F)-1:
    print('Error')

print(F)
