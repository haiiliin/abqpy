This class provides a way to supply items to widgets, such as AFXComboBox and AFXList.

![](../SIMACAERefImages/gui-afxitemprovider.png)

### AFXItemProvider

###   

### AFXItemProvider(initialItems='')  
![](../IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| initialItems | String | '' | Sequence string with initial items. |

### append

###   

### append(str)  
![](../IconsReference/butix_top_wline.png)

Appends a string to the item string.

| **Argument** | **Type** | **Default** | **Description** |
| str | String |   |   |

### append

###   

### append(ch)  
![](../IconsReference/butix_top_wline.png)

Appends a character to the item string.

| **Argument** | **Type** | **Default** | **Description** |
| ch | String |   |   |

### empty

###   

### empty()  
![](../IconsReference/butix_top_wline.png)

Returns True if the item string is empty.

### getItems

###   

### getItems()  
![](../IconsReference/butix_top_wline.png)

Returns a sequence string that contains all of the provider's items.

### getVersion

###   

### getVersion()  
![](../IconsReference/butix_top_wline.png)

Returns the version of provider's items.

### reset

###   

### reset(sz=0)  
![](../IconsReference/butix_top_wline.png)

Clears the contents of the item string and reallocates space.

| **Argument** | **Type** | **Default** | **Description** |
| sz | Int | 0 |   |

### setItems

###   

### setItems(newItems)  
![](../IconsReference/butix_top_wline.png)

Sets all of the providers's items, clearing any previous items first.

| **Argument** | **Type** | **Default** | **Description** |
| newItems | String |   | Sequence string with new items. |



 |