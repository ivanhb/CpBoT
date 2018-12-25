var my_config = {
  'border_pattern': 'img/circle_pattern.png',
  'main_eng_title': "Ivan Heibi's website",
  'intro_eng_text' : `
      This is Ivan Heibi's website, and you will find all the essential info about him in this page ... That's not giving you a lot of detail, is it? So in case you are still here and interested, just move down on this page and check out all the information you want.
      <p>In case you want to ask me for any further info, just feel free to contact me.</p>
    `,

  'intro_arabic_text' : `
"هذا هو موقع إيفان هيبي ، وسوف تجد كل المعلومات الأساسية عنه في هذه الصفحة ... وهذا لا يعطيك الكثير من التفاصيل ، أليس كذلك؟ اقرأ المزيد عن: السيرة الذاتية الخاصة بي هنا ، أو انتقل لرؤية ما أعمل عليه هنا ، أو حتى تحقق من مدى رغبتي في قضاء وقت انتشاري هنا. نعم ، هناك شيء هناك للجميع. بعد هذه الروابط والتنقل في هذه الصفحة ستقودك خلال كل ما تحتاج إلى معرفته عني."
  `,

  'list_menu' : {
    'items': {
      'Page Top':{'href': '#_top', 'default':true},
      'Short Biography':{'href': '#short_bio_top'},
      'Main Projects':{'href': '#projects_list_top'},
      'Publications':{'href': '#publications_list_top'},
      'Activities':{'href': '#activities_list_top'}
    }
  },

  'bio_section': {
    'title': "A  short  Bio",
    'content': `
      <p> I'm Ivan, a computer scientist and a Ph.D student at the <a class="section_content_link" href="https://www.unibo.it/it">University of Bologna</a> mostly dealing with Semantic web technologies specially in scholarly publishing contexts. I am working under The <a class="section_content_link" href="http://www.ficlit.unibo.it/it">Department of Classic Philology and Italian Studies (FICLIT)</a> and specially involved in the new <a class="section_content_link" href="https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge">Digital Humanities course</a>.</p>
      <p>I was born in Israel, my father is arab and my mother is Italian. Luckily, I gained both as mother languages and I like to maintain both the cultures active in my lifestyle. After my high school graduation at the age of 18, I moved to Italy and to the University of Bologna to study computer science, and I have successfully completed my bachelor and master degree.</p>
      <p>On the last year I worked with David Shotton from the University of Oxford, and Silvio Peroni of the University of Bologna as a research fellow under the <a class="section_content_link" href="http://opencitations.net/">OpenCitations project</a>: a scholarly infrastructure organization dedicated to open scholarship and the publication of open bibliographic and citation data by the use of Semantic Web (Linked Data) technologies, and engaged in advocacy for semantic publishing and open citations. My contribution was basically based on studying and developing applications for data visualization and data querying of RDF datasets of scholarly articles/papers. Here you will find a link to my CV in case you want to have more details about me.</p>
      <table width="100%" class="ui celled table"><tbody><tr><td></div></div></td><td><div class="extra_elem"><a class="git_repo_link" target="_blank" href="https://www.slideshare.net/slideshow/embed_code/key/BHStiTN572u9ju"><i class="file big icon"></i> Take a look at my CV</a><div></div></div></td></tr></tbody></table>
    `,
    'links':[
      {'href': 'https://twitter.com/ivanheib','a_class':'ui circular blue twitter icon button','content':'<i class="twitter big icon"></i>'},
      {'href': 'https://www.facebook.com/ivanhb.ita','a_class':'ui circular blue facebook icon button','content':'<i class="facebook big icon"></i>'},
      {'href': 'https://www.linkedin.com/in/ivan-heibi-738317a3','a_class':'ui circular blue linkedin icon button','content':'<i class="linkedin big icon"></i>'},
      {'href': 'https://github.com/ivanhb','a_class':'ui circular blue github icon button','content':'<i class="github big icon"></i>'}
    ]
  },

  'section': [
    {
      'id': 'projects',
      'title': 'Main projects',
      'type': 'publication',
      'items': [
        {
          'title': {'value':'OSCAR','label':'','class':'publication'},
          'subtitle': {'value':'The general Search Application for Rdf data specially designed for Open Citations','label':'','class':'publication'},
          'content':{'value': `
            A user friendly search platform applicable for any triplestore endpoint.
            This idea came out with regard to the OpenCitations project, which contains an open repository of scholarly citation data in RDF format, we would like to make accesible for any user to search and explore. The current version of the tool is integrated inside the OpenCitations web interface.
            One of the main characteristics of OSCAR is its adaptability to work with any other RDF triplestore. It is possible to configure OSCAR to work with a particular endpoint by configuring a particular JSON document, which specifies how the SPARQL queries are sent to that endpoint, and how the returned query results should be visualized, according to the predefined tabular view that OSCAR provides.
          `,'label':'','class':'publication'},
          'extra': [
            [
              {
                'value':'<a class="git_repo_link" target="_blank" href="http://opencitations.net/search"><i class="star big icon"></i> Try it on OpenCitations website</a>',
                'class': 'extra_elem'
              },
              {
                'value':'<a class="git_repo_link" target="_blank"  href="https://github.com/opencitations/oscar"><i class="github alternate big icon"></i> Go to repository</a>',
                'class': 'extra_elem'
              },
              /*
              {
                'value': `
                  <span class="__oc_badge__" input="10.1186/1756-8722-6-59" type="br" preview="citation_count"></span>
                  `
              }*/
            ]
          ]
          /*
          'extra':[
            ['','<a class="git_repo_link" style="float:right;" href="https://github.com/opencitations/oscar"><i class="github alternate medium icon"></i> Go to repository</a>']
          ]
          */
        },
        {
          'title': {'value':'LUCINDA','label':'','class':'publication'},
          'subtitle': {'value':'An RDF data browser Javascript-based application.','label':'','class':'publication'},
          'content': {'value': `
            This idea came out with regard to the OpenCitations project, which contains an open repository of scholarly citation data in RDF format, we would like to make accesible for any user to search and explore. LUCINDA uses OSCAR and its features: which is a general search application for rdf data specially designed for open citations.
            One of the main characteristics of LUCINDA is its adaptability to work with any other RDF triplestore. In order to do that there is a configuration file that could be adopted according to the SPARQL endpoint we wish to integrate.
          `,'label':'','class':'publication'},
          'extra': [
            [
              {
                'value':'<a class="git_repo_link" target="_blank" href="http://opencitations.net/browser/ra/6932102"><i class="star big icon"></i> Try it on OpenCitations website</a>',
                'class': 'extra_elem'
              },
              {
                'value':'<a class="git_repo_link" target="_blank"  href="https://github.com/opencitations/lucinda"><i class="github alternate big icon"></i> Go to repository</a>',
                'class': 'extra_elem'
              }
            ]
          ]
        },
        {
          'title': {'value':'EMA','label':'','class':'publication'},
          'subtitle': {'value':'The Email Mining Application','label':'','class':'publication'},
          'content': {'value': `
            A visual web-based framework meant for Email data analysis in digital and forensic investigation. The image legendOnion.png shows the general Framework architecture. Each different analysis will be contained in a unique folder inside the static/ folder. This architecture is meant to be flexible for updates and additional integration of new components and data analysis.
          `,'label':'','class':'publication'},
          'extra': [
            [
              {'value':''},
              {
                'value':'<a class="git_repo_link" target="_blank"  href="https://github.com/ivanhb/EMA"><i class="github alternate big icon"></i> Go to repository</a>',
                'class': 'extra_elem'
              }
            ]
          ]
        }
      ]
    },
    {
      'id': 'publications',
      'title': 'Publications',
      'items': [
        {
          'content':{
            'value': 'Heibi I., Peroni S., Shotton D. (2018) OSCAR: A Customisable Tool for Free-Text Search over SPARQL Endpoints. In: González-Beltrán A., Osborne F., Peroni S., Vahdati S. (eds) Semantics, Analytics, Visualization. SAVE-SD 2017, SAVE-SD 2018. Lecture Notes in Computer Science, vol 10959. Springer, Cham </br><a class="git_repo_link" target="_blank"  href="https://doi.org/10.1007/978-3-030-01379-0_9">https://doi.org/10.1007/978-3-030-01379-0_9</a>'
          },
          'subtitle':{
            'value': ''
          }
        },
        {
          'content':{
            'value': '<u>Upcoming:</u> Heibi I., Peroni S., Shotton D. Enabling text search on SPARQL-endpoints through OSCAR. Data Science. </br><a class="git_repo_link" target="_blank"  href="data/paper/oscar-datascience2019/oscar-datascience2019.html">Preview version</a>'
          },
          'subtitle':{
            'value': ''
          }
        }
      ],
    },

    {

      'id': 'activities',
      'title': 'Activities',
      'items':
        [
          {
              'title': {
                'value': 'WikiCite 2018',
                'label': 'Event: '
              },
              'subtitle': [
                {
                  'value': 'Berkeley, California, USA',
                  'label': 'Location: '
                },
                {
                  'value': '27 - 29 November 2018',
                  'label': 'Date: '
                },
                {
                  'value': `
                  Presenting a talk about: OSCAR and LUCINDA with Wikidata
                  `,
                  'label': 'Contribution:'
                }
              ],
              'content':[
                {
                  'value': `
                      WikiCite 2018 is a 3-day conference, summit, and hack day dedicated to the vision of creating an open repository of bibliographic data to support the citation and fact-checking needs of Wikimedia projects, and possibly, to serve as an open infrastructure for research, education, and information quality across the web.
                  `,
                  'label': 'Description'
                }
              ],
              'extra': [
                [
                  {
                    'value':'<a class="git_repo_link" target="_blank" href="https://meta.wikimedia.org/wiki/WikiCite_2018"><i class="linkify big icon"></i> Conference website</a>',
                    'class': 'extra_elem'
                  },
                  {
                    'value':'<a class="git_repo_link" target="_blank" href="https://docs.google.com/presentation/d/1lM8HDFUytUEQ2vu603yJ0R1T8qTdsx8q50o5vP9y2so/edit?usp=sharing"><i class="eye big icon"></i> View the presentation</a>',
                    'class': 'extra_elem'
                  },
                  {
                    'value':'<a class="git_repo_link" target="_blank" href="https://opencitations.github.io/lucinda/example/wikidata/browser.html?browse=Q30536251"><i class="star big icon"></i> LUCINDA demo for Wikidata</a>',
                    'class': 'extra_elem'
                  },
                  {
                    'value':'<a class="git_repo_link" target="_blank" href="https://opencitations.github.io/oscar/example/v2/wikidata.html"><i class="star big icon"></i> OSCAR demo for Wikidata</a>',
                    'class': 'extra_elem'
                  }
                ]
              ]
          },
          {
              'title': {
                'value': 'Workshop on Open Citations',
                'label': 'Event: '
              },
              'subtitle': [
                {
                  'value': 'Bologna, Italy',
                  'label': 'Location: '
                },
                {
                  'value': '3 - 5 September 2018',
                  'label': 'Date: '
                },
                {
                  'value': `
                  Staff of the Workshop
                  `,
                  'label': 'Contribution:'
                }
              ],
              'content':[
                {
                  'value': `
                      About 500 million open bibliographic citations are available on the web. We invite to this workshop researchers, scholarly publishers, funders, policy makers, and opening citations advocates, interested in the widespread adoption of practises for creation, reuse and improvement of open citation data.
                  `,
                  'label': 'Description'
                }
              ],
              'extra': [
                [
                  {'value':''},
                  {
                    'value':'<a class="git_repo_link" target="_blank"  href="https://workshop-oc.github.io/index.html"><i class="linkify big icon"></i> Workshop website</a>',
                    'class': 'extra_elem'
                  }
                ]
              ]
          },
          {
              'title': {
                'value': 'The Semantics, Analytics, Visualisation: Enhancing Scholarly Dissemination (SAVE-SD) Workshop co-located with The Web Conference',
                'label': 'Event: '
              },
              'subtitle': [
                {
                  'value': 'Lyon, France',
                  'label': 'Location: '
                },
                {
                  'value': '23 - 27 April 2018',
                  'label': 'Date: '
                },
                {
                  'value': `Presenting a talk about <a class="section_content_link" target="_blank" href="https://doi.org/10.1007/978-3-030-01379-0_9">OSCAR: A Customisable Tool for Free-Text Search over SPARQL Endpoints.</a>`,
                  'label': 'Contribution:'
                }
              ],
              'content':[
                {
                  'value': `
                      The International World Wide Web Conference Committee (IW3C2), is the organization that manages The Web Conference (former WWW Conference) series. This series aims to provide the world a premier forum for discussion and debate about the evolution of the Web, the standardization of its associated technologies, and the impact of those technologies on society and culture.
                  `,
                  'label': 'Description'
                }
              ],
              'extra': [
                [
                  {'value':''},
                  {
                    'value':'<a class="git_repo_link" target="_blank"  href="https://save-sd.github.io/2018/index.html"><i class="linkify big icon"></i> Workshop website</a>',
                    'class': 'extra_elem'
                  }
                ]
              ]
          }
        ]
    }
  ]
}
