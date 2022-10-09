intro = """
                    <div class="columns portfolio-item">
                        <div class="item-wrap">

                            <a href="#modal-"""
mid="""" title="">
                                <img alt="" src="images/"""
ending = """.JPG">
                                <div class="overlay">
                                    <div class="portfolio-item-meta">
                                        <h5>Coffee</h5>
                                        <p>Illustrration</p>
                                    </div>
                                </div>
                                <div class="link-icon"><i class="icon-plus"></i></div>
                            </a>

                        </div>
                    </div>
                    <!-- item end -->
"""

for i in range(40,67):
    print(intro,end="")
    print(str(i),end="")
    print(mid,end="")
    print("img"+str(i),end="")
    print(ending,end="\n\n")
