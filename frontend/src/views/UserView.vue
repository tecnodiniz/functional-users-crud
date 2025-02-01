<template>
  <v-card class="pa-5">
    <v-card-title class="green">
      {{ user.username }}
    </v-card-title>
    <v-col>
      <div class="text-left">
        <v-list-item> <span class="green">ID</span>: {{ user._id }} </v-list-item>
        <v-list-item> <span class="green">STATUS: </span> {{ user.active }} </v-list-item>
        <v-list-item> <span class="green">ROLES: </span> {{ user.roles }} </v-list-item>
        <v-list-item> <span class="green">PREFERENCES:</span> {{ user.preferences }} </v-list-item>
        <v-list-item>
          <span class="green">CREATEDAT: </span> {{ formatDate(user.created_ts) }}
        </v-list-item>
        <v-list-item
          ><span class="green">UPDATED AT:</span>
          {{ user.updated_ts ? formatDate(user.updated_ts) : '' }}</v-list-item
        >
      </div>
    </v-col>

    <v-divider></v-divider>
    <v-card-actions>
      <v-btn variant="plain" @click="handleDelete">Delete</v-btn>
    </v-card-actions>
  </v-card>

  <DialogComponet :dialog="dialog" :text="d_text" :title="d_title" @close="dialog = false" />

  <ConfirmDialogComponent
    :dialog="confirm"
    :del="delUser"
    text="Delete user?"
    title="Confirm"
    @close="confirm = false"
    @confirm-delete="deleteUser"
  />
</template>

<script setup>
import DialogComponet from '@/components/DialogComponet.vue'
import ConfirmDialogComponent from '@/components/ConfirmDialogComponent.vue'
import { get_user, user_delete } from '@/services/api'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const user = ref({})
const confirm = ref(false)
const delUser = ref(false)

const dialog = ref(false)
const d_text = ref('')
const d_title = ref('')

onMounted(() => {
  getUser(route.params.id)
})

const getUser = async (id) => {
  get_user(id)
    .then((response) => (user.value = response.data.user))
    .catch((error) => console.log(error))
}

const formatDate = (timestamp) => {
  const date = new Date(timestamp * 1000)
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true,
  }

  return date.toLocaleDateString('en-US', options) // US Format
}

const handleDelete = () => {
  delUser.value = true
  confirm.value = true
}

const deleteUser = async () => {
  user_delete(route.params.id)
    .then((response) => {
      d_text.value = response.data.msg
      d_title.value = 'Message'
      dialog.value = true
      confirm.value = false
      delUser.value = false

      setTimeout(() => {
        location.href = '/'
      }, 2500)
    })
    .catch((error) => {
      console.log(error)
      d_text.value = error.message
      d_title.value = 'Error'
      dialog.value = true
    })
}
</script>
