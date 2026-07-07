---
layout: null
---

<meta name="color-scheme" content="dark light">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

[← Back to Home](/index.md)

## How I built a High Performance cache implementation
*Apr 4, 2026 | Category: systems*

It's been a week since I open-sourced my 4th cpp-based project. 

My project is called [**velocache**](https://github.com/tecnolgd/velocache), inspired by the aim of making it a High Performance cache tool for terminal applications. This project uses a doubly linked-list(DLL) as the main data structure for storing and retriving the cache data. 

The DLL is accompanied by unordered map for key-value storage to achieve ***O(1)*** lookup time. This cache implementation uses **LRU eviction policy** for the cache behavior and functionality. 

In short, LRU eviction could be understood as evicting or deleting the least recently used/oldest data in the cache. In the context of this project, it could be the least recently accessed data in the file.    

### The things needed for consideration were as follows:   

- The storage of the data (key-value pairs) had to be done in such a way that the least recently used data would be at the top of the file.     
- The cache or simply the DLL must be loaded every time a new session of `PUT` (i.e, storing the data into the cache).    
- The latest data needed to be tracked and repositioned to make sure the eviction happens only to the least recently used data.

### The solution    

1. The function to save the data into the file is written in such a way that it starts writing the contents of the DLL (the key-value pairs) in a **Tail-to-Head** order. This makes sure the least recently use element always stays at the top of the file since writing onto a file starts from the first line.      
2. A seperate function is implemented to make sure the data from the file is loaded to the DLL(called **Hydration**) which makes sure the user is interacting with the data from the latest session. 

    The solution no 1. does the work of making sure the latest data is always at the end of the file using a custom function which performs a **plucking** operation when a value is retrieved by its corresponding key. This operation plucks the retrived node(key-value pair) and places it at the start of the DLL making sure the DLL chain is not broken while plucking.     
3.  The tracking happens by the property of the DLL where the recenty used data is always at the start of the DLL and the least recently used one at the end of the DLL.      

### The Future of this project

The main motivation behind building a cache implementation, was to understand basic cache working and the logic involving the LRU eviction using a file as a medium to to see in real time how the replacing and eviction of data is performed. 

But this won't stop here. I hope of making this simple cache implementation into a **pluggable tool which would work as a High Perf. cache for terminal tools or applications** which involve usage of external or simulated cache(yeah, I am not sure about this now).  

*Detailed breakdown would be available shortly.* 

Stay tuned for future updates.
