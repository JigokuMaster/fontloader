/*
based on this Qt utility
https://gist.github.com/elpuri/756413

*/


#include <s32std.h>
#include <coemain.h>
#include <w32std.h>
#include <badesca.h>
#include <gulutil.h>
#include <Python.h>
#include <symbian_python_ext_util.h>


static PyObject* load_font(PyObject *self, PyObject* args)
{

    PyObject* font_fp;
    if (!PyArg_ParseTuple(args, "U", &font_fp))
    {
        return NULL;
    }

    TPtrC SFont_Path((TUint16*) PyUnicode_AsUnicode(font_fp),PyUnicode_GetSize(font_fp));

    int fontId;
    int err = CCoeEnv::Static()->ScreenDevice()->AddFile(SFont_Path, fontId);
    if(err == KErrNone)
    {
        return Py_BuildValue("i",fontId);
    }
    else
    {
        return SPyErr_SetFromSymbianOSErr(err); 
    }
    
    Py_INCREF(Py_None);
    return Py_None;
    
}



static PyObject* unload_font(PyObject *self, PyObject* args)
{

    int fontId;
    if (!PyArg_ParseTuple(args, "i", &fontId))
    {
        return NULL;
    }


    CCoeEnv::Static()->ScreenDevice()->RemoveFile(fontId);
    Py_INCREF(Py_None);
    return Py_None;
    
}


static PyMethodDef methodDesc[] = {
	{"load", load_font, METH_VARARGS, ""},
	{"unload", unload_font, METH_VARARGS, ""},
	{NULL, NULL, 0, NULL},
    };



DL_EXPORT(void) MODULE_INIT_FUNC()
{


    PyObject* module= Py_InitModule3("_fontloader", methodDesc,"");  
    if (!module)
    {
      return;
    }
}




