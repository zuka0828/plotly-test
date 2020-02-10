#!/usr/bin/python

# Setup:
#   $ pip install plotly numpy
# Reference: https://plot.ly/python/gantt/

import plotly.figure_factory as ff

# Reference: Debian releases https://ja.wikipedia.org/wiki/Debian
df = [
    # Debian 8
    dict(Task="Debian 8", Resource="Debian_testing",
         Start="2013-05-04", Finish="2015-04-25"),
    dict(Task="Debian 8", Resource="Debian_stable",
         Start="2015-04-25", Finish="2018-06-17"),
    dict(Task="Debian 8", Resource="Debian_LTS",
         Start="2018-06-17", Finish="2020-06-30"),
    dict(Task="Debian 8", Resource="Debian_ELTS",
         Start="2020-06-30", Finish="2021-06-30"),
    # Debian 9
    dict(Task="Debian 9", Resource="Debian_testing",
         Start="2015-04-25", Finish="2017-06-17"),
    # NOTE: Finish date not decided
    dict(Task="Debian 9", Resource="Debian_stable",
         Start="2017-06-17", Finish="2020-06-17"),
    dict(Task="Debian 9", Resource="Debian_LTS",
         Start="2020-06-17", Finish="2022-06-17"),
    dict(Task="Debian 9", Resource="Debian_ELTS",
         Start="2022-06-17", Finish="2023-06-17"),
    # Debian 10
    dict(Task="Debian 10", Resource="Debian_testing",
         Start="2017-06-17", Finish="2019-07-06"),
    # NOTE: Finish date not decided
    dict(Task="Debian 10", Resource="Debian_stable",
         Start="2019-07-06", Finish="2022-07-06"),
    dict(Task="Debian 10", Resource="Debian_LTS",
         Start="2022-07-06", Finish="2024-07-06"),
    dict(Task="Debian 10", Resource="Debian_ELTS",
         Start="2024-07-06", Finish="2025-07-06"),

    # CIP kernel (4.4)
    # v4.4.42-cip1 release date:
    # https://git.kernel.org/pub/scm/linux/kernel/git/cip/linux-cip.git/tag/?h=v4.4.42-cip1
    # TBD: Multiple stages? Temporally allocate two years as stage1
    dict(Task="CIP kernel (4.4)", Resource="CIP_kernel_stage1",
         Start="2017-01-17", Finish="2019-01-17"),
    dict(Task="CIP kernel (4.4)", Resource="CIP_kernel_stage2",
         Start="2019-01-17", Finish="2027-01-17"),
    # CIP Core (Debian 8)
    # https://gitlab.com/cip-project/cip-core/deby was created on Oct. 18th 2017
    dict(Task="CIP Core (Debian 8)", Resource="CIP_core_stage1",
         Start="2017-10-18", Finish="2020-06-30"),
    dict(Task="CIP Core (Debian 8)", Resource="CIP_core_stage2",
         Start="2020-06-30", Finish="2027-10-18"),
    # CIP Core (Debian 9)
    # https://gitlab.com/cip-project/cip-core/isar-cip-core was created on Jan. 3th 2019
    dict(Task="CIP Core (Debian 9)", Resource="CIP_core_stage1",
         Start="2019-01-03", Finish="2022-06-17"),
    dict(Task="CIP Core (Debian 9)", Resource="CIP_core_stage2",
         Start="2022-06-17", Finish="2029-01-03"),
    # CIP kernel (4.19)
    # v4.19.13-cip1 release date:
    # https://git.kernel.org/pub/scm/linux/kernel/git/cip/linux-cip.git/tag/?h=v4.19.13-cip1
    dict(Task="CIP kernel (4.19)", Resource="CIP_kernel_stage1",
         Start="2019-01-11", Finish="2021-01-11"),
    dict(Task="CIP kernel (4.19)", Resource="CIP_kernel_stage2",
         Start="2021-01-11", Finish="2029-01-11"),
    # CIP Core (Debian 10)
    dict(Task="CIP Core (Debian 10)", Resource="CIP_core_stage1",
         Start="2019-07-06", Finish="2024-07-06"),
    dict(Task="CIP Core (Debian 10)", Resource="CIP_core_stage2",
         Start="2024-07-06", Finish="2029-07-06"),
]

colors = dict(
    Debian_testing = "rgb(150, 150, 150)",
    Debian_stable = "rgb(0, 0, 255)",
    Debian_LTS = "rgb(100, 100, 255)",
    Debian_ELTS = "rgb(200, 200, 255)",
    CIP_kernel_stage1 = "rgb(255, 0, 0)",
    CIP_kernel_stage2 = "rgb(255, 150, 150)",
    CIP_core_stage1 = "rgb(0, 200, 0)",
    CIP_core_stage2 = "rgb(150, 200, 150)",
)

fig = ff.create_gantt(
    df,
    title="Time Line of Long-term Linux Projects",
    colors=colors,
    index_col="Resource",
    group_tasks=True,
    show_colorbar=True,
    showgrid_x=True,
    showgrid_y=True,
)
fig.show()
