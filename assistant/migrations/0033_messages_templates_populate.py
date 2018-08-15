# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-28 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0032_auto_20170928_1408'),
    ]

    operations = [
        migrations.RunSQL(
            [(
             "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
             ['assistant_assistants_startup_normal_renewal_html',
              'Renouvellement des mandats des assistant\u00b7e\u00b7s',
              '<p>{% autoescape off %}</p>\r\n\r\n<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u2019effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\n</p>\r\nCordialement,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
              'HTML', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
            "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
            ['assistant_assistants_startup_normal_renewal_txt',
            'Renouvellement des mandats des assistant\u00b7e\u00b7s',
            '<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u2019effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\n</p>\r\nCordialement,<br />\r\nOsis UCLouvain',
            'PLAIN', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
            "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
            ['assistant_assistants_startup_normal_renewal_html',
            'Assistants mandates renewal',
            '<p>{% autoescape off %}</p>\r\n\r\n<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun. It is conducted by electronic means only.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\n</p>\r\nRegards,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
            'HTML', 'en'])],
        ),
        migrations.RunSQL(
            [(
            "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
            ['assistant_assistants_startup_normal_renewal_txt',
            'Assistants mandates renewal',
            '<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun. It is conducted by electronic means only.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\n</p>\r\nRegards,<br />\r\nOsis UCLouvain',
            'PLAIN', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_assistants_startup_except_renewal_html',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u2019effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nDans votre cas, vous avez atteint le nombre maximum d\u0027ann\u00e9es de mandat autoris\u00e9es pour demander un renouvellement normal, donc si vous le souhaitez et si vous avez des circonstances exceptionnelles qui le justifient, vous pouvez introduire une demande de renouvellement exceptionnel d\u0027un an. Pour cela, nous vous demandons d\u0027apporter une argumentation approfondie pour faciliter la d\u00e9cision des autorit\u00e9s sur le caract\u00e8re exceptionnel ou non de ces circonstances.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\nNous restons \u00e0 votre disposition pour toute information compl\u00e9mentaire.</p><br />\r\nCordialement,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_assistants_startup_except_renewal_txt',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u2019effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nDans votre cas, vous avez atteint le nombre maximum d\u0027ann\u00e9es de mandat autoris\u00e9es pour demander un renouvellement normal, donc si vous le souhaitez et si vous avez des circonstances exceptionnelles qui le justifient, vous pouvez introduire une demande de renouvellement exceptionnel d\u0027un an. Pour cela, nous vous demandons d\u0027apporter une argumentation approfondie pour faciliter la d\u00e9cision des autorit\u00e9s sur le caract\u00e8re exceptionnel ou non de ces circonstances.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\nNous restons \u00e0 votre disposition pour toute information compl\u00e9mentaire.</p><br />\r\nCordialement,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_assistants_startup_except_renewal_html',
                 'Assistants mandates renewal',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun. It is conducted by electronic means only.<br />\r\n<br />\r\nIn your case, you have reached the maximum number of years allowed to apply for a normal renewal. You may however, if you so desire and if it can be justified by exceptional circumstances, apply for a one-off renewal period of one year.  Therefore, we ask you to provide detailed arguments in order to facilitate the decision of the authorities on the exceptional nature or not of these circumstances.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\nWe remain at your disposal should you need any additional information.<br />\r\n</p>Regards,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_assistants_startup_except_renewal_txt',
                 'Assistants mandates renewal',
                 '<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun. It is conducted by electronic means only.<br />\r\n<br />\r\nIn your case, you have reached the maximum number of years allowed to apply for a normal renewal. You may however, if you so desire and if it can be justified by exceptional circumstances, apply for a one-off renewal period of one year.  Therefore, we ask you to provide detailed arguments in order to facilitate the decision of the authorities on the exceptional nature or not of these circumstances.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\nWe remain at your disposal should you need any additional information.<br />\r\n</p>Regards,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_reviewers_startup_html',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nNous venons de lancer la proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }}.<br />\r\nNous attirons votre attention sur le fait que les assistant\u00b7e\u00b7s ayant une \u00e9ch\u00e9ance au 30-06-{{ last_ending_year }} n\u0027ont pas \u00e9t\u00e9 int\u00e9gr\u00e9s \u00e0 la proc\u00e9dure.<br />\r\nElle s\u0027effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\nPour rappel, toute demande de renouvellement introduite par un\u00b7e assistant\u00b7e doit \u00eatre mise dans le circuit et ne peut \u00eatre bloqu\u00e9e sous pr\u00e9texte que les avis sont n\u00e9gatifs car l\u0027assistant\u00b7e a, dans ce cas, le droit d\u0027introduire un recours selon l\u0027article 50 du RAMCS.</p><br />\r\nCordialement,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_reviewers_startup_txt',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nNous venons de lancer la proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }}.<br />\r\nNous attirons votre attention sur le fait que les assistant\u00b7e\u00b7s ayant une \u00e9ch\u00e9ance au 30-06-{{ last_ending_year }} n\u0027ont pas \u00e9t\u00e9 int\u00e9gr\u00e9s \u00e0 la proc\u00e9dure.<br />\r\nElle s\u0027effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\nPour rappel, toute demande de renouvellement introduite par un\u00b7e assistant\u00b7e doit \u00eatre mise dans le circuit et ne peut \u00eatre bloqu\u00e9e sous pr\u00e9texte que les avis sont n\u00e9gatifs car l\u0027assistant\u00b7e a, dans ce cas, le droit d\u0027introduire un recours selon l\u0027article 50 du RAMCS.</p><br />\r\nCordialement,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_reviewers_startup_html',
                 'Assistants mandates renewal',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nWe have just started the procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }}.<br />\r\nWe would like to draw your attention to the fact that the assistants with a 30-06-{{ last_ending_year }} deadline have not been integrated in the procedure.<br />\r\nIt is conducted by electronic means only.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\nAs a reminder, any renewal application made by an assistant must be put in the circuit and cannot be blocked on the pretext of negative opinions since the assistant has, in this case, the right of appeal against the decision under article 50 of the RAMCS.</p><br />\r\nRegards,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_reviewers_startup_txt   ',
                 'Assistants mandates renewal',
                 '<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nWe have just started the procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }}.<br />\r\nWe would like to draw your attention to the fact that the assistants with a 30-06-{{ last_ending_year }} deadline have not been integrated in the procedure.<br />\r\nIt is conducted by electronic means only.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be​​​​​​​/assistants<br />\r\n<br />\r\nAs a reminder, any renewal application made by an assistant must be put in the circuit and cannot be blocked on the pretext of negative opinions since the assistant has, in this case, the right of appeal against the decision under article 50 of the RAMCS.</p><br />\r\nRegards,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_phd_supervisor_html',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u0027effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nVous recevez ce message en tant que superviseur de th\u00e8se pour {{ assistant }}.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure et compl\u00e9ter votre avis, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be/assistants/phd_supervisor/assistants<br />\r\n</p>Cordialement,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_phd_supervisor_txt',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u0027effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nVous recevez ce message en tant que superviseur de th\u00e8se pour {{ assistant }}.<br />\r\n<br />\r\nPour acc\u00e9der \u00e0 la proc\u00e9dure et compl\u00e9ter votre avis, il vous suffit de suivre le lien suivant: https://osis.uclouvain.be/assistants/phd_supervisor/assistants<br />\r\n</p>Cordialement,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_phd_supervisor_html',
                 'Assistants mandates renewal',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun.  It is conducted by electronic means only.<br />\r\n<br />\r\nYou receive this message as a supervisor for {{ assistant }}.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be/assistants/phd_supervisor/assistants</p><br />\r\nRegards,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_phd_supervisor_txt   ',
                 'Assistants mandates renewal',
                 '<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun.  It is conducted by electronic means only.<br />\r\n<br />\r\nYou receive this message as a supervisor for {{ assistant }}.<br />\r\n<br />\r\nIn order to gain access to the procedure, simply click on the following link: https://osis.uclouvain.be/assistants/phd_supervisor/assistants</p><br />\r\nRegards,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_dean_assistant_decline_html',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u0027effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nVous recevez ce message car {{ assistant }} a d\u00e9clin\u00e9 sa demande de renouvellement.<br />\r\n</p>Cordialement,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_dean_assistant_decline_txt',
                 'Renouvellement des mandats des assistant\u00b7e\u00b7s',
                 '<p>Bonjour {{ first_name}} {{ last_name}},<br />\r\n<p>Ceci est un message automatique g\u00e9n\u00e9r\u00e9 par le serveur OSIS – Merci de ne pas y r\u00e9pondre.<br />\r\n<br />\r\nLa proc\u00e9dure de renouvellement des mandats des assistant\u00b7e\u00b7s dont le contrat arrive \u00e0 \u00e9ch\u00e9ance entre le {{ start_date }} et le {{ end_date }} vient de d\u00e9buter. Elle s\u0027effectue int\u00e9gralement par voie \u00e9lectronique.<br />\r\n<br />\r\nVous recevez ce message car {{ assistant }} a d\u00e9clin\u00e9 sa demande de renouvellement.<br />\r\n</p>Cordialement,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'fr-be'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_dean_assistant_decline_html',
                 'Assistants mandates renewal',
                 '<p>{% autoescape off %}</p>\r\n\r\n<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun.  It is conducted by electronic means only.<br />\r\n<br />\r\nYou receive this message because {{ assistant }} has declined his renewal application.</p><br />\r\nRegards,<br />\r\nOsis UCLouvain<br />\r\n{% endautoescape %}',
                 'HTML', 'en'])],
        ),
        migrations.RunSQL(
            [(
                "INSERT INTO osis_common_messagetemplate (reference, subject, template, format, language) VALUES (%s, %s, %s, %s, %s);",
                ['assistant_dean_assistant_decline_txt',
                 'Assistants mandates renewal',
                 '<p>Hello {{ first_name}} {{ last_name}},<br />\r\n<p>This is an automatic message generated by the OSIS server – Please do not reply to this message.<br />\r\n<br />\r\nThe procedure for renewing the mandates of assistants whose contract expires between the {{ start_date }} and the {{ end_date }} has just begun.  It is conducted by electronic means only.<br />\r\n<br />\r\nYou receive this message because {{ assistant }} has declined his renewal application.</p><br />\r\nRegards,<br />\r\nOsis UCLouvain',
                 'PLAIN', 'en'])],
        ),
    ]










