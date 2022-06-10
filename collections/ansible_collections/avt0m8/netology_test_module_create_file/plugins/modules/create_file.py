#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: create_file

short_description: This is my test module for file creation

version_added: "1.0.0"

description: This is my netology practice test module for file creation.

options:
    path:
        description: This is relative path to file should be created or rewritten to send to the test module.
        required: true
        type: str
    content:
        description:
            - Content to be written to target file.
            - Default content is empty. If not provided, target file content would be erased.
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - avt0m8.netology_test_module_create_file.my_doc_create_file

author:
    - Stas Arts (@stasarts)
'''

EXAMPLES = r'''
# Pass with empty file
- path: Test with a path only
  avt0m8.netology_test_module_create_file.create_file:
    path: ./create_file_test.txt

# Pass with fulfilled file
- name: Test with created/rewritten and fulfilled file
  my_namespace.my_collection.my_test:
    path: ./create_file_test.txt
    content: "outstanding content"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original content param that was passed in.
    type: str
    returned: always
    sample: 'outstanding content'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 
        - 'file was created'
        - 'file was rewritten'
'''

import os
from ansible.module_utils.basic import AnsibleModule


# Check if file exists
def file_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


# Check is the file content as provided
def check_content(path, content):
    with open(path, 'r') as file:
        file_content = file.read()
    if file_content == content:
        return True
    else:
        return False


# Write content to file
def write_content_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
    return True


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default=' ')
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        if not os.path.exists(module.params['path']):
            result['changed'] = True
        module.exit_json(**result)

    if not file_exists(module.params['path']):
        write_content_to_file(module.params['path'], module.params['content'])
        result['changed'] = True
        result['original_message'] = "File {path} was successfully created".format(path=module.params['path'])
        result['message'] = 'file was created'
    else:
        if check_content(module.params['path'], module.params['content']):
            result['changed'] = False
            result['original_message'] = "File {path} exists with the same content".format(path=module.params['path'])
            result['message'] = 'file exists'
        else:
            write_content_to_file(module.params['path'], module.params['content'])
            result['changed'] = True
            result['original_message'] = "File {path} was successfully rewritten".format(path=module.params['path'])
            result['message'] = 'file was rewritten'

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
