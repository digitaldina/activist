<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<template>
  <div
    class="grid grid-cols-1 gap-6 sm:grid-cols-2 sm:grid-rows-2 md:grid-cols-3 md:grid-rows-1 lg:gap-12"
  >
    <ImageLogo
      imageName="WikimediaDE"
      imageLink="https://www.wikimedia.de"
      :aria-label="
        $t('i18n.components.grid_supporters.wikimedia_de_logo_aria_label')
      "
    />
    <ImageLogo
      imageName="WikimediaRS"
      imageLink="https://wikimedia.rs"
      :aria-label="
        $t('i18n.components.grid_supporters.wikimedia_rs_logo_aria_label')
      "
    />
    <ImageLogo
      imageName="ImpactHub"
      imageLink="https://belgrade.impacthub.net"
      :aria-label="
        $t(
          'i18n.components.grid_supporters.impact_hub_belgrade_logo_aria_label'
        )
      "
    />
  </div>
</template>
