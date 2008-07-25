# -*- coding: utf-8 -*-
"""
plone.app.z3cform

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id$
"""
import plone.z3cform.templates
import zope.app.pagetemplate.viewpagetemplatefile


class Macros(plone.z3cform.templates.Macros):
    template = zope.app.pagetemplate.viewpagetemplatefile.ViewPageTemplateFile(
        'macros.pt')

    def __getitem__(self, key):
        return self.template.macros[key]
