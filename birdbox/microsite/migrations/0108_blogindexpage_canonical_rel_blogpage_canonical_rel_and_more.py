# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 4.2.11 on 2024-04-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("microsite", "0107_alter_micrositesettings_site_theme"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogindexpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="blogpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="externalredirectionpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="faqpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="generalpurposepage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="innovationscontentpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="longformarticlepage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="productpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="protocoltestpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
        migrations.AddField(
            model_name="structuralpage",
            name="canonical_rel",
            field=models.URLField(
                blank=True,
                help_text='Value to use within a &lt;link rel="canonical" ...&gt; tag in the head of this page, to indicate a preferred URL for this page elsewhere. Only set this if you know what you are doing. See <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#canonical">MDN docs</a>.',
            ),
        ),
    ]