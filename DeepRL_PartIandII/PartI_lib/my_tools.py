#@title MyTools

import json
import os
import torch

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def create_dir(path,name,overwrite = False):
    if not os.path.exists(path):
        os.mkdir(path)
    directory_contents = os.listdir(path+"/")
    if not overwrite:
        folder = [itn for itn in directory_contents if os.path.isdir(path+'/'+itn)]
        matching = [s for s in folder if name in s]

        vals = []

        for s in matching:
            if s == name:
                for itn in matching:
                    v = find_between(itn, '(', ')')
                    if v != "":
                        vals.append(int(v))
                        
                vals.sort()
                k = 1
                for v in vals:
                    if v != k:
                        break
                    k += 1

                name += ('('+str(k)+')')


                break

    if not os.path.exists(path+"/"+name):
        os.mkdir(path+"/"+name)
    return path+'/'+name

def set_name(arch,BatchSize,exploration_threshold,exploration_threshold_min,exploration_decay,discount_factor,LearningRate,LearningRateDecay):
    new_name = arch+"_" + str(BatchSize) + "_" + str(exploration_threshold).replace('.', '') + "_" + \
            str(exploration_threshold_min).replace('.', '') + "_" + \
            ("{:.0e}".format(exploration_decay)).replace(
                '.', '')+"_"+str(discount_factor).replace('.', '')+"_"+("{:.0e}".format(LearningRate)).replace(
                '.', '')+"_"+str(LearningRateDecay).replace('.', '')
    return new_name

# def get_reference(pathName):
#     images = torch.load(pathName+'/imgs.ref')
#     labels = torch.load(pathName+'/labels.ref')
#     return images, labels




# class model_loader:
#     def __init__(self, name):
#         self.name = name

#         self.models = []
#         self.import_from_json()

#         self.length = len(self.models)
#         self.current = -1

    
#     def next(self):
#         self.current += 1
#         return self.define_model_attributes(self.models[self.current])


#     def import_from_json(self):
#         f = open(self.name)
#         print("Importing model from: "+self.name)
#         data = json.load(f)
#         try:
#             data = data["models"]
#         except:
#            print("Empty json file.")
#            f.close()
#            return

#         for j in range(len(data)):
#             self.models.append(data[j])

#         f.close()

#     def define_model_attributes(self, data):
#         new_name = data["model_name"]+"_" + \
#             ("{:.0e}".format(data["learning_rate"])).replace(
#                 '.', '')+"_"+str(data["learning_rate_decay"]).replace('.', '')+"_"+str(data["regularization"]).replace('.', '')
#         print(new_name)
#         model_attributes = {
#             "arch_name": data["arch_name"],
#             "name": new_name,
#             "batch_size": 16                 if(data.get("batch_size")          == None)  else data["batch_size"],
#             "number_of_epochs": 25           if(data.get("number_of_epochs")    == None)  else data["number_of_epochs"],
#             "learning_rate": 1e-4            if(data.get("learning_rate")       == None)  else data["learning_rate"],
#             "regularization": 0              if(data.get("regularization")      == None)  else data["regularization"],
#             "pretrained": False              if(data.get('pretrained')          == None)  else data['pretrained'],
#             "learning_rate_decay": 0.97      if(data.get("learning_rate_decay") == None)  else data["learning_rate_decay"],
#             "epc_per_report": 5              if(data.get("epc_per_report")      == None)  else data["epc_per_report"],
#             "report_path": "results"         if(data.get("report_path")         == None)  else data["report_path"],
#             "freeze_features": False         if(data.get("freeze_features")     == None)  else data["freeze_features"]
#         }

#         return model_attributes


# ######## metrics

