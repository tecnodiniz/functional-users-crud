<template>
  <div class="text-center pa-4">
    <v-dialog v-model="dialog" width="auto">
      <v-card max-width="400" prepend-icon="mdi-update" :text="text" :title="title">
        <template v-slot:actions>
          <v-btn class="ms-auto" text="Ok" @click="$emit('close')"></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { toRef } from 'vue'
const props = defineProps(['dialog', 'text', 'title'])

const dialog = toRef(props, 'dialog')
</script>
