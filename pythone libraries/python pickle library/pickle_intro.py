# what are pickle in python
'''the "pickle" module inplements a fundamental, but powerful algorithm for serializing and de-serializing and de-serializing a python
    object structure.'''
#storing data with pickle
'''
        we can pickle objects with the following data types:
        1. Booleans,
        2. Integers,
        3. Floats,
        4. Complex numbers,
        5.(normal and unicode) Strings,
        6. Tuples,
        7. Lists,
        8. Sets, and
        9. Dictionaries.
'''
''' to use pickle, start by importing it in python.

    pickle have two main methods. the first one is 'dump',which
    dumps an object to a file object and the second one is load,
    which loads an oject from a file object.
'''
#python pickle functions
'''
    dump() - this function is called to serialize an object hierachy.
    load() - this functionis called to de-serialize a data stream.
    '''
#pickling with dump()
'''
    pickling data is done via the fump() function. it accepts data and
    a file object.
    the dump() function then serializes the data and writes it to the file.
    .the syntax of dump() is as follows.
        syntax : dump(obj,file)

        """    import pickle
                example= {1:'4',2:'2',3:'7'}
                pickle_wirte= open("text.txt","wb")
                pickle.dump(example,pickle_write)
                pickle_write.close()
    note: obj:- object ot be picked.
          file:-file objext where picked data will be written
         """'''

    
