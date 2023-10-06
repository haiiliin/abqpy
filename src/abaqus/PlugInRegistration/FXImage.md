Abaqus

GUI Toolkit Reference

All Classes

FXImage

Image class

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fximage.png)

### FXImage(a, pix=None, opts=0, w=1, h=1)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create an image.

| **Argument** | **Type** | **Default** | **Description** |
| a | FXApp |   |   |
| pix |   | None |   |
| opts | Int | 0 |   |
| w | Int | 1 |   |
| h | Int | 1 |   |

### blend(color, sharpen=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Blends the icon with the specified color; should only be used on icons that support an alpha channel, for example, PNG.

| **Argument** | **Type** | **Default** | **Description** |
| color | FXColor |   |   |
| sharpen | Bool | True |   |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create image resource.

Reimplemented from FXId.

Reimplemented in FXIcon.

### destroy()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Destroy image resource.

Reimplemented from FXId.

Reimplemented in FXIcon.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach image resource.

Reimplemented from FXId.

Reimplemented in FXIcon.

### getOptions()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

To get to the option flags.

### getPixel(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get pixel at x,y.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### render()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Render the image from client-side pixel buffer.

Reimplemented in FXIcon.

### resize(w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Resize pixmap to the specified width and height.

Reimplemented from FXDrawable.

Reimplemented in FXIcon.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int |   |   |
| h | Int |   |   |

### scale(w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Rescale pixels image to the specified width and height.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int |   |   |
| h | Int |   |   |

### setPixel(x, y, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change pixel at x,y.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |
| color | FXColor |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Image rendering hints**

| **IMAGE_KEEP** | 

Keep pixel data in client.

 |
| **IMAGE_OWNED** | 

Pixel data is owned by image.

 |
| **IMAGE_DITHER** | 

Dither image to look better.

 |
| **IMAGE_NEAREST** | 

Turn off dithering and map to nearest color.

 |
| **IMAGE_ALPHA** | 

Data has alpha channel.

 |
| **IMAGE_OPAQUE** | 

Force opaque background.

 |
| **IMAGE_ALPHACOLOR** | 

Override transparancy color.

 |
| **IMAGE_SHMI** | 

Using shared memory image.

 |
| **IMAGE_SHMP** | 

Using shared memory pixmap.

 |
| **IMAGE_ALPHAGUESS** | 

Guess transparency color from corners.

 |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.

Use this form to provide feedback on this help topic. To get product support or to provide product feedback, go to [Frequently Asked Questions](https://3ds.one/PO). For support for online purchased solutions, go to [Online Purchase Support](https://3ds.one/Q8).

\* Required

Subject:

Feedback on User Assistance

*

I acknowledge I have read and I hereby accept the [privacy policy](https://www.3ds.com/privacy-policy) under which my personal data will be used by Dassault Systèmes.

Thank you for your comments. We will contact you if we have questions regarding your feedback.

Sincerely,  
The Dassault Systèmes User Assistance Team

Dialog for Cookie

Allow to use Cookie for saving your settings ?