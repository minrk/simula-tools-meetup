# 02 - Namespaces

In this module we will look namespaces which is a very powerful feature of logging.
We have the following file tree

```
├── main.py
└── parent
    ├── __init__.py
    ├── first_child.py
    └── second_child
        ├── __init__.py
        ├── first_grand_child.py
        └── second_grand_child.py
```

and for each module we have a function called `do_something` with one `info` message and one `debug` message.
We will look into how we can set different log levels on different modules. 