# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:49:24 2018

@author: Pshypher
"""

XML_TAG = """
<abc>
    <xyz> Mother </xyz>
    <pqr> Father </pqr>
    <lmn> Brothers </lmn>
    <def> Sisters </def>
</abc>
"""
ANOTHER_XML_TAG = "<abc>\n<xyz> 12 Monkeys </abc>\n</xyz>"

def parse_tag(tags_str):
    """Splits a tag into its opening, closing tag and contents.Returns a tuple."""
    
    tags_str = tags_str.strip()
    
    left_bracket = tags_str[0]
    right_bracket_sub = tags_str.find('>')
    right_bracket = tags_str[right_bracket_sub]
    start_tag = tags_str[:right_bracket_sub+1]
    tag_name_str = start_tag[1:right_bracket_sub]
    end_tag_sub = tags_str.find(left_bracket + '/' + tag_name_str +
                                right_bracket)
    end_tag = tags_str[end_tag_sub:end_tag_sub+len(start_tag)+2].strip()
    content_str = tags_str[right_bracket_sub+1:end_tag_sub].strip()
    
    return start_tag,end_tag,content_str

def valid_xml_tag(tags_str):
    """
    >>> valid_xml_tag(XML_TAG)
    True
    >>> valid_xml_tag(ANOTHER_XML_TAG)
    False
    """
    if not tags_str:
        return True
    if tags_str.isalnum():
        return True
    else:
        start_tag,end_tag,tags_str = parse_tag(tags_str)
        return start_tag == end_tag[:1]+end_tag[2:] and \
    valid_xml_tag(tags_str)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()