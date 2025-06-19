ds=[10,7,9,25,300,5,6,8,4,3,2,1]
solonnhat=-1
vitrisolonnhat=-1
for idx,value in enumerate(ds):
    if solonnhat<value:
        solonnhat=value
        vitrisolonnhat=idx


print("vi tri cua so lon nhat la: ",vitrisolonnhat)
print("so lon nhat la: ",solonnhat)        
    