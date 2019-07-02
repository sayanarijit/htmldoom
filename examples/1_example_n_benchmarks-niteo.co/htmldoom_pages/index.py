from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders
from htmldoom_pages.layout import render_document

contents = _render(
    e.nav(class_="navbar navbar-light sticky-top navbar-expand-lg")(
        e.div(class_="container")(
            e.a(href="/", class_="navbar-brand")(
                e.img(
                    src="https://niteo.co/static_niteo_co/images/logo.svg",
                    width="120",
                    height="30",
                    alt="Niteo",
                )
            ),
            e.button(
                class_="navbar-toggler",
                type_="button",
                data_toggle="collapse",
                data_target="#navbarResponsive",
                aria_controls="navbarSupportedContent",
                aria_expanded="false",
                aria_label="Toggle navigation",
            )(e.span(class_="navbar-toggler-icon")),
            e.div(class_="collapse navbar-collapse", id_="navbarResponsive")(
                e.ul(class_="navbar-nav ml-auto")(
                    e.li(class_="nav-item")(
                        e.a(class_="nav-link", href="/projects")("Projects")
                    ),
                    e.li()(e.a(class_="nav-link", href="/about")("About")),
                    e.li(class_="nav-item")(
                        e.a(class_="nav-link", href="/team")("Team")
                    ),
                    e.li(class_="nav-item")(
                        e.a(class_="nav-link", href="/careers")("Careers")
                    ),
                    e.li(class_="nav-item")(
                        e.a(href="http://blog.niteo.co/", class_="nav-link")("Blog")
                    ),
                    e.li(class_="nav-item")(
                        e.a(class_="nav-link", href="/contact")("Contact")
                    ),
                )
            ),
        )
    ),
    b.comment(" HOME "),
    e.section(class_="headline")(
        e.video(
            "playsinline",
            "autoplay",
            "muted",
            poster="https://niteo.co/static_niteo_co/video/niteo_website_video.jpg",
        )(
            e.source(
                src="https://niteo.co/static_niteo_co/video/niteo_website_video.webm",
                type_="video/webm",
            ),
            e.source(
                src="https://niteo.co/static_niteo_co/video/niteo_website_video.mp4",
                type_="video/mp4",
            ),
        ),
        e.div(class_="container")(
            e.div(class_="row justify-content-center")(
                e.div(class_="col-md-9 text-center")(
                    e.h1(class_="text-white")("Empowering Small Businesses"),
                    e.h3(class_="text-white")(
                        "Niteo is a decade old SaaS studio full of bright ideas, building smart solutions that empower small businesses online."
                    ),
                    e.a(
                        href="/projects",
                        class_="btn btn-primary btn-lg d-block d-sm-inline mr-sm-2 mt-2",
                    )("View Our Projects"),
                    e.a(
                        href="/team",
                        class_="btn btn-outline-primary btn-lg d-block d-sm-inline ml-sm-2 mt-3 mt-sm-2 text-white",
                    )("Meet Our Team"),
                )
            )
        ),
    ),
    b.comment(" END HOME "),
    b.comment(" VALUES "),
    e.section()(
        e.div(class_="container")(
            e.div(class_="row")(
                e.div(class_="col-md text-center")(
                    e.h1()("Our Values"),
                    e.p()(
                        "These values are at the core of our company. ",
                        e.br(),
                        " ",
                        e.a(href="/about")("Learn more about Niteo ..."),
                    ),
                )
            ),
            e.div(class_="row justify-content-between")(
                e.div(class_="col-2 d-none d-lg-block")(
                    e.div(class_="row justify-content-center")(
                        e.div(class_="col wow rotateInDownRight", data_wow_delay=".3s")(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_openness.svg",
                                class_="img-fluid niteo-value mx-auto d-block",
                                alt="openness",
                            )
                        )
                    )
                ),
                e.div(class_="col-2 d-none d-lg-block")(
                    e.div(class_="row justify-content-center")(
                        e.div(class_="col wow rotateInDownRight", data_wow_delay=".3s")(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_fairness.svg",
                                class_="img-fluid niteo-value mx-auto d-block",
                                alt="fairness",
                            )
                        )
                    )
                ),
                e.div(class_="col-2 d-none d-lg-block")(
                    e.div(class_="row justify-content-center")(
                        e.div(class_="col wow rotateIn", data_wow_delay=".3s")(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_curiosity.svg",
                                class_="img-fluid niteo-value mx-auto d-block",
                                alt="curiosity",
                            )
                        )
                    )
                ),
                e.div(class_="col-2 d-none d-lg-block")(
                    e.div(class_="row justify-content-center")(
                        e.div(class_="col wow rotateInDownLeft", data_wow_delay=".3s")(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_results.svg",
                                class_="img-fluid niteo-value mx-auto d-block",
                                alt="results",
                            )
                        )
                    )
                ),
                e.div(class_="col-2 d-none d-lg-block")(
                    e.div(class_="row justify-content-center")(
                        e.div(class_="col wow rotateInDownLeft", data_wow_delay=".3s")(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_agility.svg",
                                class_="img-fluid niteo-value mx-auto d-block",
                                alt="agility",
                            )
                        )
                    )
                ),
            ),
            e.div(class_="row justify-content-between")(
                e.div(class_="col-lg-2 text-center")(
                    e.div(class_="row justify-content-center")(
                        e.div(
                            class_="col-8 col-sm-5 col-md-4 d-block d-lg-none mt-3 mt-lg-0"
                        )(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_openness.svg",
                                class_="img-fluid",
                                alt="openness",
                            )
                        )
                    ),
                    e.span(class_="btn btn-lg btn-outline btn-values my-4")("Openness"),
                ),
                e.div(class_="col-lg-2 text-center")(
                    e.div(class_="row justify-content-center")(
                        e.div(
                            class_="col-8 col-sm-5 col-md-4 d-block d-lg-none mt-5 mt-lg-0"
                        )(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_fairness.svg",
                                class_="img-fluid",
                                alt="fairness",
                            )
                        )
                    ),
                    e.span(class_="btn btn-lg btn-outline btn-values my-4")("Fairness"),
                ),
                e.div(class_="col-lg-2 text-center")(
                    e.div(class_="row justify-content-center")(
                        e.div(
                            class_="col-8 col-sm-5 col-md-4 d-block d-lg-none mt-5 mt-lg-0"
                        )(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_curiosity.svg",
                                class_="img-fluid",
                                alt="curiosity",
                            )
                        )
                    ),
                    e.span(class_="btn btn-lg btn-outline btn-values my-4")(
                        "Curiosity"
                    ),
                ),
                e.div(class_="col-lg-2 text-center")(
                    e.div(class_="row justify-content-center")(
                        e.div(
                            class_="col-8 col-sm-5 col-md-4 d-block d-lg-none mt-5 mt-lg-0"
                        )(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_results.svg",
                                class_="img-fluid",
                                alt="Results",
                            )
                        )
                    ),
                    e.span(class_="btn btn-lg btn-outline btn-values my-4")("Results"),
                ),
                e.div(class_="col-lg-2 text-center")(
                    e.div(class_="row justify-content-center")(
                        e.div(
                            class_="col-8 col-sm-5 col-md-4  d-block d-lg-none mt-5 mt-lg-0"
                        )(
                            e.img(
                                src="https://niteo.co/static_niteo_co/images/homepage/homepage_agility.svg",
                                class_="img-fluid",
                                alt="agility",
                            )
                        )
                    ),
                    e.span(class_="btn btn-lg btn-outline btn-values my-4")("Agility"),
                ),
            ),
        )
    ),
    b.comment(" END VALUES "),
    b.comment(" HANDBOOK "),
    e.section()(
        e.div(class_="container")(
            e.div(class_="row align-items-center")(
                e.div(class_="col-lg-8 col-md-8")(
                    e.div(class_="jumbotron")(
                        e.h1()("The Niteo Handbook"),
                        e.p()(
                            "For the last decade, we have been accumulating the knowledge and practicalities of running an Open Source business within our walled-off intranet. At our 10th Anniversary Party we realized that it was time that we made this valuable information public with the intent of helping people in similar positions. "
                        ),
                        e.p()(
                            "This Handbook offer us an opportunity to clarify what Niteo is and how we operate. It allows greater transparency to our partners, potential new team members, and the wider Open Source community. "
                        ),
                        e.div(class_="text-center")(
                            e.a(
                                href="https://github.com/niteoweb/handbook",
                                class_="btn btn-primary btn-lg mt-4",
                                target="_blank",
                            )(" View Our Handbook")
                        ),
                    )
                ),
                e.div(
                    class_="col px-5 mx-5 mx-md-0 px-md-0  wow bounceIn",
                    data_wow_delay=".4s",
                )(
                    e.img(
                        src="https://niteo.co/static_niteo_co/images/handbook_big.svg",
                        class_="img-fluid",
                        alt="Handbook",
                    )
                ),
            )
        )
    ),
    b.comment(" END HANDBOOK "),
    b.comment(" TECHNOLOGIES "),
    e.section(class_="technologies")(
        e.div(class_="container")(
            e.div(class_="row")(
                e.div(class_="col text-center")(e.h1()("Technologies We Love"))
            ),
            e.div(class_="row")(
                e.div(class_="col-lg-3 offset-lg-1")(
                    e.div(
                        class_="jumbotron logo python wow slideInUp",
                        data_wow_delay=".1s",
                    )(
                        e.img(
                            src="https://niteo.co/static_niteo_co/images/homepage/tech_logo_python.svg",
                            alt="python",
                            class_="img-fluid mx-auto d-block",
                        )
                    )
                ),
                e.div(class_="col-lg-3 offset-lg-1")(
                    e.div(
                        class_="jumbotron logo wordpress wow slideInUp",
                        data_wow_delay=".1s",
                    )(
                        e.img(
                            src="https://niteo.co/static_niteo_co/images/homepage/tech_logo_wp.svg",
                            alt="wordpress",
                            class_="img-fluid mx-auto d-block",
                        )
                    )
                ),
            ),
            e.div(class_="row offset-top")(
                e.div(class_="col-lg-3 offset-lg-3")(
                    e.div(
                        class_="jumbotron logo pyramid wow slideInDown",
                        data_wow_delay=".1s",
                    )(
                        e.img(
                            src="https://niteo.co/static_niteo_co/images/homepage/tech_logo_pyramid.svg",
                            alt="pyramid",
                            class_="img-fluid mx-auto d-block",
                        )
                    )
                ),
                e.div(class_="col-lg-3 offset-lg-1")(
                    e.div(
                        class_="jumbotron logo woocommerce wow slideInDown",
                        data_wow_delay=".2s",
                    )(
                        e.img(
                            src="https://niteo.co/static_niteo_co/images/homepage/tech_logo_woocommerce.svg",
                            alt="woocommerce",
                            class_="img-fluid mx-auto my-auto d-block",
                        )
                    )
                ),
            ),
        )
    ),
    b.comment(" END TECHNOLOGIES "),
    b.comment(" BLOG, CONTACT "),
    e.section(class_="technologies")(
        e.div(class_="container")(
            e.div(class_="row")(
                e.div(class_="col-lg")(
                    e.h1(class_="mt-5")("Read Our Blog"),
                    e.div(id_="blog-fallback")(
                        e.a(
                            href="https://blog.niteo.co/",
                            class_="btn btn-primary btn-lg",
                        )(" Visit Our Blog ")
                    ),
                    e.div(class_="row my-5 my-lg-1", id_="blog-post-0")(
                        e.div(class_="col-sm-4 my-2 my-sm-1 blog-image")(
                            e.a(href="#", target="_blank")(
                                e.img("alt", src="#", class_="img-fluid")
                            )
                        ),
                        e.div(class_="col-sm-8")(
                            e.p(class_="lead blog-title")(
                                e.a(href="#", target="_blank")
                            ),
                            e.p(class_="blog-excerpt"),
                        ),
                    ),
                    e.div(class_="row my-5 my-lg-1", id_="blog-post-1")(
                        e.div(class_="col-sm-4 my-2 my-sm-1 blog-image")(
                            e.a(href="#", target="_blank")(
                                e.img("alt", src="#", class_="img-fluid")
                            )
                        ),
                        e.div(class_="col-sm-8")(
                            e.p(class_="lead blog-title")(
                                e.a(href="#", target="_blank")
                            ),
                            e.p(class_="blog-excerpt"),
                        ),
                    ),
                ),
                e.div(class_="col-lg")(
                    e.div(class_="jumbotron")(
                        e.div(class_="row")(
                            e.div(class_="col text-center")(e.h1()("Contact Us"))
                        ),
                        e.div(class_="row justify-content-lg-center")(
                            e.div(class_=" col-lg-8 text-center")(
                                e.p()(
                                    "Niteo has team members from Slovenia, Ukraine, Romania, India, and the Philippines. You can reach us at anytime below."
                                )
                            )
                        ),
                        e.div(class_="contact text-center")(
                            e.a(href="/contact", class_="btn btn-primary btn-lg")(
                                "Contact Us"
                            )
                        ),
                    )
                ),
            )
        )
    ),
    b.comment(" END BLOG, CONTACT "),
    b.comment(" FOOTER "),
    e.footer(class_="bg-secondary")(
        e.div(class_="container")(
            e.div(class_="row")(
                e.div(class_="col-md")(
                    e.h6()(e.a(href="/projects")("Projects")),
                    e.ul(class_="list-unstyled")(
                        e.li()(e.a(href="/projects#flagship")("Flagship")),
                        e.li()(e.a(href="/projects#open-source")("Open Source")),
                        e.li()(e.a(href="/projects#sold")("Sold")),
                        e.li()(e.a(href="/projects#client")("Client")),
                    ),
                ),
                e.div(class_="col-md")(
                    e.h6()(e.a(href="/about")("About")),
                    e.ul(class_="list-unstyled")(
                        e.li()(e.a(href="/about#company")("Company")),
                        e.li()(e.a(href="/about#timeline")("Timeline")),
                        e.li()(e.a(href="/about#giving-back")("Giving Back")),
                    ),
                ),
                e.div(class_="col-md")(
                    e.h6()(e.a(href="/team")("Team")),
                    e.ul(class_="list-unstyled")(
                        e.li()(e.a(href="/team#people")("People")),
                        e.li()(e.a(href="/team#irl")("IRL")),
                        e.li()(e.a(href="/team#conferences")("Conferences")),
                    ),
                ),
                e.div(class_="col-md")(
                    e.h6()(e.a(href="/careers")("Careers")),
                    e.ul(class_="list-unstyled")(
                        e.li()(e.a(href="/careers#work-coworkers")("Work & Coworkers")),
                        e.li()(e.a(href="/careers#management")("Management")),
                        e.li()(e.a(href="/careers#benefits")("Benefits")),
                        e.li()(e.a(href="/careers#open-jobs")("Open Jobs")),
                    ),
                ),
                e.div(class_="col-md")(
                    e.h6()(e.a(href="/contact")("Contact")),
                    e.ul(class_="list-unstyled")(
                        e.li()(e.a(href="/contact#support")("Support")),
                        e.li()(e.a(href="/contact#address")("Address")),
                        e.li()(e.a(href="/legal/privacy")("Legal")),
                        e.li(class_="social")(
                            e.a(
                                class_="mr-1",
                                href="https://www.facebook.com/teamniteo",
                                target="_blank",
                            )(e.i(class_="fa fa-facebook-f")),
                            e.a(
                                class_="ml-1",
                                href="https://twitter.com/teamniteo",
                                target="_blank",
                            )(e.i(class_="fa fa-twitter")),
                        ),
                    ),
                ),
            ),
            e.div(class_="row h-100 justify-content-center align-items-center mt-4")(
                e.p()(e.small()("© 2007 - 2019 Niteo "))
            ),
        )
    ),
    b.comment(" END FOOTER "),
    e.script(src="https://niteo.co/static_niteo_co/main.js"),
    b.comment(" Fanstatic body css/js here "),
    e.script()(
        b"""
        var loadJS = function (url, implementationCode) {
          // url: URL of external file,
          // implementationCode: code to be called after script is loaded,

          var scriptTag = document.createElement('script');
          scriptTag.src = url;

          scriptTag.onload = implementationCode;
          scriptTag.onreadystatechange = implementationCode;

          document.body.appendChild(scriptTag);
        };

        // Global site tag (gtag.js) - Google Analytics
        var googleTag = function () {
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'UA-116005149-1');
        };

        var loadGoogleTag = function () {
          loadJS('https://www.googletagmanager.com/gtag/js?id=UA-116005149-1', googleTag);
        };

        if(typeof optin !== 'undefined') {
          optin("analytics", loadGoogleTag);
        } else {
          loadGoogleTag();
        }
        """
    ),
    e.script()(
        b"""
        document.addEventListener("DOMContentLoaded", function(event) {
          if(typeof gdprCookieNotice !== 'undefined') {
            gdprCookieNotice({
              statement: 'https://niteo.co/legal/cookies',
              analytics: ['_gat', '_ga', '_gid', '_gat_gtag_UA_116005149_1'],
              providers: {
                essential: "Cloudflare (security)",
                analytics: "Google Analytics",
              }
            });
          }
        });
        """
    ),
)


@renders(e.body()("{contents}"))
def render_body(data):
    return {"contents": contents}


def render(data):
    return render_document(data=data, body_renderer=render_body)


if __name__ == "__main__":
    print(render({"doctitle": "Niteo - Empowering small businesses online since '07"}))
