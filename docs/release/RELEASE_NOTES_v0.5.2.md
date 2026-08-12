# Chenhaoran Portal v0.5.2

## Fixed

- Removes the obsolete desktop rule that hid every right-navigation item after Search.
- Makes the visible desktop selector `中文 EN 日本語` appear after Search at the far right of the navigation bar.
- Adds a regression test that prevents the hidden-right-item rule from returning.

## Boundaries

- This is a portal presentation patch only. It does not change any Framework, System, Skill, local runtime, Study, data, account, or external integration.
- The selector remains same-page switching only. It does not use browser-language detection or automatic redirects.
