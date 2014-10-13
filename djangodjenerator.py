#!/usr/bin/env python
"""Django model to XMI converter
by Jaron Crocker

Make sure your set the SysPath to point to the correct settings in your project folder.

"python djangodjenerator.py YOURAPP > output.xmi"

Django model to DOT (Graphviz) converter
by Antonio Cavedoni <antonio@cavedoni.org>

__version__ = "0.8"
__svnid__ = "$Id$"
__license__ = "Python"
__author__ = "Antonio Cavedoni <http://cavedoni.com/>"
__contributors__ = [
   "Stefano J. Attardi <http://attardi.org/>",
   "limodou <http://www.donews.net/limodou/>",
   "Carlo C8E Miron",
   "Andre Campos <cahenan@gmail.com>",
   "Justin Findlay <jfindlay@gmail.com>",
   "Alexander Houben <alexander@houben.ch>",
   "Christopher Schmidt <crschmidt@metacarta.com>",
   "Jaron Crocker <stroshowjaron@hotmail.com>"
   ]
"""

import getopt
import sys
import os
import datetime
import time
sys.path.append("C:\Users\Jcrocker\Desktop\DjangoUML\PRJ")
from django.core.management import setup_environ
import settings
setup_environ(settings)
import xml.etree.ElementTree as ET
import inspect

from django.template import Template, Context
from django.db import models
from django.db.models import get_models
from django.db.models.fields.related import \
    ForeignKey, OneToOneField, ManyToManyField

try:
    from django.db.models.fields.generic import GenericRelation
except ImportError:
    from django.contrib.contenttypes.generic import GenericRelation

m = 0
mr = 0
a = 0
c = 0
dictionary = {}
ass = 0
assend = 0
com = 0
metadata = ""

def generate_xmi(app_labels, **kwargs):

    global m
    global mr
    global a
    global c
    global ass
    global assend
    global dictionary
    global com
    
    disable_fields = kwargs.get('disable_fields', False)
    include_models = kwargs.get('include_models', [])
    exclude_models = kwargs.get('exclude_models', [])

    builder = ET.TreeBuilder()
    builder.start("XMI", {"xmi.version":"1.2", "xmlns:UML":"org.omg.xmi.namespace.UML", "timestamp":datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')})
    builder.start("XMI.header", {})
    builder.start("XMI.metamodel", {"xmi.name":"UML", "xmi.version":"1.4"})
    builder.end("XMI.metamodel")
    builder.end("XMI.header")
    builder.start("XMI.content", {})
    builder.start("UML:Model", {"xmi.id":"Model", "name":"MyProject", "isSpecification":"false", "isRoot":"false", "isLeaf":"false"})
    builder.start("UML:Namespace.ownedElement", {})
    
    builder.start("UML:Package", {"xmi.id":"Package1", "name":"Django Data Types", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.start("UML:Namespace.ownedElement", {})
    builder.start("UML:DataType", {"xmi.id":"DDT.1", "name":"Date", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.2", "name":"Char 8", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.3", "name":"Char 32", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.4", "name":"Char 128", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.5", "name":"Char 255", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.6", "name":"Char 1024", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.7", "name":"Text", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.8", "name":"URL", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.9", "name":"DateTime", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.10", "name":"Float", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.11", "name":"Time", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.12", "name":"Email", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.13", "name":"Foreign Key", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.14", "name":"AutoField", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.start("UML:DataType", {"xmi.id":"DDT.15", "name":"ManyToManyField", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.end("UML:DataType")
    builder.end("UML:Namespace.ownedElement")
    builder.end("UML:Package")

    builder.start("UML:Package", {"xmi.id":"Package2", "name":"MyApplication", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
    builder.start("UML:Namespace.ownedElement", {})
    
    for app_label in app_labels:
        app = models.get_app(app_label)
                            
    for appmodel in get_models(app):
        # consider given model name ?
        def consider(model_name):
            return (not include_models or model_name in include_models) and (not model_name in exclude_models)
        
        if not consider(appmodel._meta.object_name):
            continue
                        
        """ Create Class XMI Node """
        builder.start("UML:Class", {"xmi.id":"C."+str(c), "name":appmodel.__name__, "visibility":"public", "isSpecification":"false", "isRoot":"false", "isLeaf":"false"})
        builder.start("UML:Classifier.feature", {})
        dictionary[""+appmodel.__name__] = "C."+str(c)
        c+=1
        
        """ Loops through the fields adds them to the current Class node as attributes """
        def addXMIattributes():
            builder.start("UML:Attribute", {"xmi.id":"A."+str(a), "name":field.name.title().replace ("_", " "), "visibility":"public", "isSpecification":"false", "ownerScope":"instance", "changeability":"changeable", "targetScope":"instance"})
            builder.start("UML:StructuralFeature.multiplicity", {})
            builder.start("UML:Multiplicity", {"xmi.id":"M."+str(m)})
            builder.start("UML:Multiplicity.range", {})
            builder.start("UML:MultiplicityRange", {"xmi.id":"MR."+str(mr), "lower":"1", "upper":"1"})
            builder.end("UML:MultiplicityRange")
            builder.end("UML:Multiplicity.range")
            builder.end("UML:Multiplicity")
            builder.end("UML:StructuralFeature.multiplicity")
            if (str(type(field).__name__) is "DateField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.1"})
            elif (str(type(field).__name__) is "CharField" and field.max_length == 8):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.2"})
            elif (str(type(field).__name__) is "CharField" and field.max_length == 32):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.3"})
            elif (str(type(field).__name__) is "CharField" and field.max_length == 128):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.4"})
            elif (str(type(field).__name__) is "CharField" and field.max_length == 255):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.5"})
            elif (str(type(field).__name__) is "CharField" and field.max_length == 1024):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.6"})
            elif (str(type(field).__name__) is "TextField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.7"})
            elif (str(type(field).__name__) is "URLField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.8"})
            elif (str(type(field).__name__) is "DateTimeField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.9"})
            elif (str(type(field).__name__) is "FloatField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.10"})
            elif (str(type(field).__name__) is "TimeField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.11"})
            elif (str(type(field).__name__) is "EmailField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.12"})
            elif (str(type(field).__name__) is "IntegerField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"href":"http://argouml.org/profiles/uml14/default-uml14.xmi#-84-17--56-5-43645a83:11466542d86:-8000:000000000000087C"})
            elif (str(type(field).__name__) is "ForeignKey"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.13"})
            elif (str(type(field).__name__) is "AutoField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.14"})
            elif (str(type(field).__name__) is "ManyToManyField"):
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {"xmi.idref":"DDT.15"})                    
            else:
                builder.start("UML:StructuralFeature.type", {})
                builder.start("UML:DataType", {})
            builder.end("UML:DataType")
            builder.end("UML:StructuralFeature.type")
            builder.end("UML:Attribute")
            
        for field in appmodel._meta.fields:
            if not field.name == "None":
                addXMIattributes()
                m+=1
                mr+=1
                a+=1
    
        if appmodel._meta.many_to_many:
            for field in appmodel._meta.many_to_many:
                if not field.name == "None":
                    addXMIattributes()
                    m+=1
                    mr+=1
                    a+=1

        builder.end("UML:Classifier.feature")
        builder.end("UML:Class")
        
    # relations
    for appmodel in get_models(app):
        
        def add_XMI_relation(lower1="", upper1="", lower2="", upper2="", Navigability1="", Navigability2=""):

            global m
            global mr
            global a
            global c
            global ass
            global assend
            global dictionary
            global com
            
            builder.start("UML:Association", {"xmi.id":"ASS."+str(ass), "name":"", "isSpecification":"false", "isRoot":"false", "isLeaf":"false", "isAbstract":"false"})
            builder.start("UML:Association.connection", {})
            builder.start("UML:AssociationEnd", {"xmi.id":"ASSEND"+str(assend), "visibility":"public", "isSpecification":"false", "isNavigable":""+Navigability1, "ordering":"unordered", "aggregation":"none", "targetScope":"instance", "changeability":"changeable"})
            builder.start("UML:AssociationEnd.multiplicity", {})
            builder.start("UML:Multiplicity", {"xmi.id":"M."+str(m)})
            builder.start("UML:Multiplicity.range", {})
            builder.start("UML:MultiplicityRange", {"xmi.id":"MR."+str(mr), "lower":""+lower1, "upper":""+upper1})
            builder.end("UML:MultiplicityRange")
            builder.end("UML:Multiplicity.range")
            builder.end("UML:Multiplicity")
            builder.end("UML:AssociationEnd.multiplicity")
            builder.start("UML:AssociationEnd.participant", {})
            builder.start("UML:Class", {"xmi.idref":""+dictionary[appmodel.__name__]})
            builder.end("UML:Class")
            builder.end("UML:AssociationEnd.participant")
            builder.end("UML:AssociationEnd")

            mr+=1
            m+=1
            ass+=1
            assend+=1
            
            builder.start("UML:AssociationEnd", {"xmi.id":"ASSEND."+str(assend), "visibility":"public", "isSpecification":"false", "isNavigable":""+Navigability2, "ordering":"unordered", "aggregation":"none", "targetScope":"instance", "changeability":"changeable"})
            builder.start("UML:AssociationEnd.multiplicity", {})
            builder.start("UML:Multiplicity", {"xmi.id":"M."+str(m)})
            builder.start("UML:Multiplicity.range", {})
            builder.start("UML:MultiplicityRange", {"xmi.id":"MR."+str(mr), "lower":""+lower2, "upper":""+upper2})
            builder.end("UML:MultiplicityRange")
            builder.end("UML:Multiplicity.range")
            builder.end("UML:Multiplicity")
            builder.end("UML:AssociationEnd.multiplicity")
            builder.start("UML:AssociationEnd.participant", {})
            builder.start("UML:Class", {"xmi.idref":""+dictionary[""+field.rel.to.__name__]})
            builder.end("UML:Class")
            builder.end("UML:AssociationEnd.participant")
            builder.end("UML:AssociationEnd")
            builder.end("UML:Association.connection")
            builder.end("UML:Association")
            
            mr+=1
            m+=1
            ass+=1
            assend+=1
                                            
        for field in appmodel._meta.fields:
            if isinstance(field, ForeignKey):
                add_XMI_relation("0", "-1", "0", "1", "false", "true")
            elif isinstance(field, OneToOneField):
                add_XMI_relation("0", "1", "0", "1", "true", "true")

        if appmodel._meta.many_to_many:
            for field in appmodel._meta.many_to_many:
                if isinstance(field, ManyToManyField):
                    add_XMI_relation("0", "-1", "0", "-1", "true", "true")
                elif isinstance(field, GenericRelation):
                    add_XMI_relation("0", "-1", "0", "1", "false", "true")
                                    
    builder.end("UML:Namespace.ownedElement")
    builder.end("UML:Package")
    
    for appmodel in get_models(app):
        metadata = "Meta Data: " + "\n" + "\n"
        MetaDict = appmodel._meta.__dict__
        for key in MetaDict:
            if key is "abstract" or key is "app_label" or key is "db_table" or key is "db_tablespace" or key is "get_latest_by" or key is "managed" or key is "order_with_respect_to" or key is "ordering" or key is "permissions" or key is "proxy" or key is "select_on_save" or key is "unique_together" or key is "index_together" or key is "verbose_name" or key is "verbose_name_plural":
                metadata = metadata + str(key) + " = " + str(MetaDict[key]) + "\n"
        builder.start("UML:Comment", {"xmi.id":"COM."+str(com), "isSpecification":"false", "body":""+metadata})
        builder.start("UML:Comment.annotatedElement", {})
        builder.start("UML:Class", {"xmi.idref":""+dictionary[appmodel.__name__]})
        builder.end("UML:Class")
        builder.end("UML:Comment.annotatedElement")
        builder.end("UML:Comment")
        com+=1
        
    for appmodel in get_models(app):
        methoddata = "Methods: " + "\n" + "\n"
        methods = inspect.getmembers(appmodel, inspect.ismethod)
        for name, _ in methods:
            methoddata = methoddata + name + "\n"
        builder.start("UML:Comment", {"xmi.id":"COM."+str(com), "isSpecification":"false", "body":""+methoddata})
        builder.start("UML:Comment.annotatedElement", {})
        builder.start("UML:Class", {"xmi.idref":""+dictionary[appmodel.__name__]})
        builder.end("UML:Class")
        builder.end("UML:Comment.annotatedElement")
        builder.end("UML:Comment")
        com+=1
    
    builder.end("UML:Namespace.ownedElement")
    builder.end("UML:Model")
    builder.end("XMI.content")
    builder.end("XMI")
    root = builder.close()
    return ET.tostring(root)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hdi:e:",
                    ["help", "disable_fields", "include_models=", "exclude_models="])
    except getopt.GetoptError, error:
        print __doc__
        sys.exit(error)
    else:
        if not args:
            print __doc__
            sys.exit()

    kwargs = {}
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print __doc__
            sys.exit()
        if opt in ("-d", "--disable_fields"):
            kwargs['disable_fields'] = True
        if opt in ("-i", "--include_models"):
            kwargs['include_models'] = arg.split(',')
        if opt in ("-e", "--exclude_models"):
            kwargs['exclude_models'] = arg.split(',')
    print generate_xmi(args, **kwargs)

if __name__ == "__main__":
    main()
