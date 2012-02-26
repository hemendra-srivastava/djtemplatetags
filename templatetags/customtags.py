from django import template
from django.utils.html import escape
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

@register.filter
def maketable(element):
    """ [{tr params}, [{td params}, tdvalue(will be escaped)]*n ] is the format of elements """

    html = u""
    print element
    for row in element:
        for ele in row:
            
            if type(ele) == type({}):
                html += u"""
<tr """ 
                for k,v in ele.items():
                    html += u'%s="%s" ' %(k,v)
                html += u'>'
            else:
                tdvalue = ele
                if type(ele) == (type([]) or tuple):
                    params, val = ele
                    html += """
    <td """
                    for k,v in params.items():
                        html += u'%s="%s" ' %(k,v)
                    html += u'>'
                    tdvalue = val
                else:
                    html += """
    <td> """
                html += escape(str(tdvalue))
                html += " </td>"
                html += """
</tr> """

    return mark_safe(html)
