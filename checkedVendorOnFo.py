ó
mUc           @   sO   d  d l  m Z d  d l Z d  d l m Z m Z d e j f d     YZ d S(   iÿÿÿÿ(   t	   webdriverN(   t   NoSuchElementExceptiont   TimeoutExceptiont   test_vendorc           B   s#   e  Z d    Z d   Z d   Z RS(   c         C   s6   t  j   |  _ |  j j d d  |  j j d  d  S(   Nil  s   http://testing.futurumshop.nl(   R    t   Chromet   drivert   set_window_sizet   get(   t   self(    (    s3   /home/bohdan/FuturumAutoTest/click_vendor_footer.pyt   setUp   s    c         C   sI  d } d } g  |  _  x-| d k rDyô | d 7} | d k rP | d 7} d } n  | d k rl | d k rl t S|  j j d j | |   |  _ |  j  j |  j j d  d d  d    |  j j	   |  j j
 d	  } t |  d k rx |  j  D] } qñ W|  j j d
 j |   n  Wq t k
 r@|  j j d  d GHq Xq Wd  S(   Ni    i   iS   i   i   s(   //*[@id='footer']/div[4]/ul[{}]/li[{}]/at   hrefi   s"   //div[@class='breadcrumb row']//lis   /home/bohdan/{0!s}.pngs   http://futurumshop.nls   Lending page (   t   vendor_namet   FalseR   t   find_element_by_xpatht   formatt   footert   appendt   get_attributet   Nonet   clickt   find_elements_by_xpatht   lent   get_screenshot_as_fileR   R   (   R   t   lit   ult   xt   names(    (    s3   /home/bohdan/FuturumAutoTest/click_vendor_footer.pyt    test_broken_linkvendor_in_footer   s,    	

	!) c         C   s   |  j  j   d  S(   N(   R   t   quit(   R   (    (    s3   /home/bohdan/FuturumAutoTest/click_vendor_footer.pyt   tearDown*   s    (   t   __name__t
   __module__R	   R   R   (    (    (    s3   /home/bohdan/FuturumAutoTest/click_vendor_footer.pyR      s   		(   t   seleniumR    t   unittestt   selenium.common.exceptionsR   R   t   TestCaseR   (    (    (    s3   /home/bohdan/FuturumAutoTest/click_vendor_footer.pyt   <module>   s   