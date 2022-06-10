create_file_role
=========

Simple creates/rewrites file with content.

Role Variables
--------------
There is only two variables that you can redefine in your playbook.
```yaml
path: "./file.txt" # Use for relative path to file
content: "some content" # Use for content should be written to file (optional)
```
If no content provided, file will be empty.

Example Playbook
----------------

```yaml
- hosts: all
  collections:
    - avt0m8.netology_test_module_create_file
  roles:
      - create_file_role
```

License
-------

BSD

Author Information
------------------

Stas Arts