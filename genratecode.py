intro = """
            <div id="modal-"""
middle = """" class="popup-modal mfp-hide">

                <img class="scale-with-grid" src="images/"""
ending = """.jpg" alt="" />

                <div class="description-box">
                    <h4>Coffee Cup</h4>
                    <p>Proin gravida nibh vel velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit.</p>
                    <span class="categories"><i class="fa fa-tag"></i>Branding, Webdesign</span>
                </div>

                <div class="link-box">
                    <a href="http://srikrishnacommunication.com/Giridesigns.html" target="_blank">Details</a>
                    <a class="popup-modal-dismiss">Close</a>
                </div>

            </div>
            <!-- modal-01 End -->
"""
for i in range(40,67):
    print(intro,end="")
    print(str(i),end="")
    print(middle,end="")
    print("img"+str(i),end="")
    print(ending,end="\n\n")
