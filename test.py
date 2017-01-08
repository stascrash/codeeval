
# # # print (123 % 10)
# # # print (123 / 10)
# # # print (12 % 10)
# # # print (12 / 10)
# # # print (1 % 10)
# # # print (1 / 10)



# # import maya.cmds as cmds
# # import sys
# # scriptPath = '/Users/jonvarner/Desktop/FurnitureBaker/'
# # sys.path.append(scriptPath)
# # try:
# # 	from LightBaker import main
# # 	reload(main)
# # 	modelName = 'autoTest'
# # 	main.bakeFurniture(exportDirectory = modelName)
# # except Exception as e:
# # 	print e

# # #--------------
# # def getFileByExtention(path, f_ext):
# #     '''Returns Generator. all files from path that match f_ext'''
# #     if os.path.exists(path):
# #         for f in os.listdir(path):
# #             if os.path.isfile(os.path.join(path, f)):
# #                 if f.split(".")[-1] == f_ext:
# #                     yield f

# # import os
# # import maya.cmds as cmds
# # import shutil
# # import sys


# # mainDirToBake = '/Users/jonvarner/Desktop/Test_Bake_Folder/'
# # scriptPath = '/Users/jonvarner/Desktop/FurnitureBaker/'
# # sysPaths = sys.path
# # if [s for s in sysPaths if scriptPath in s]:
# #     print "Path already present"
# # else:
# #     sys.path.insert(0,scriptPath)
# # from LightBaker import main

# # def bakeDir(model):
# #     modelName = model
# #     main.bakeFurniture(exportDirectory = modelName)   

# # def getModelsToBake():
# #     models = [d for d in os.listdir(mainDirToBake) if os.path.isdir(os.path.join(mainDirToBake, d))]
# #     for model in models:
# #         cmds.file(f=True, new=True)
# #         pathtoModel = mainDirToBake + str(model) + '/'    
# #         modelFBX = [os.path.join(dirpath, f)
# #             for dirpath, dirnames, files in os.walk(pathtoModel)
# #             for f in files if f.endswith('.fbx')]
# #         cmds.file(modelFBX, i=True)
        
# #         bakeDir(model)
    
# # getModelsToBake()





# def recPermute(soFar, rest):
#     if rest == "":
#         print soFar
#     else:
#         for i in range(len(rest)):
#             next = soFar + rest[i]
#             remaining = rest.replace(rest[i],"")
#             recPermute(next, remaining)
# #recPermute("","abcd")

# def subset(nums, total, partial=[]):
#     s = sum(partial)

#     if s == total:
#         print partial
#     if s >= total:
#         return

#     for i in range(len(nums)):
#         n = nums[i]
#         remaining = nums[i+1:]
#         subset(remaining, total, partial + [n])


# total = 10
# nums = [x for x in range(total)]

# subset(nums, total)

my = [True, False, True]
con = my[2] || False

print con