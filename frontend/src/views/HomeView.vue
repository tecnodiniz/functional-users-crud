<template>
  <v-row>
    <v-col class="text-center">
      <UserFormComponent @new-user="createUser" />
      <UserTableComponent :users="users" @delete-user="deleteUser" @edit-user="editUser" />

      <DialogComponet :dialog="dialog" :text="d_text" :title="d_title" @close="dialog = false" />
    </v-col>
  </v-row>
</template>

<script setup>
import DialogComponet from '@/components/DialogComponet.vue'
import UserFormComponent from '@/components/UserFormComponent.vue'
import UserTableComponent from '@/components/UserTableComponent.vue'
import { get_users, new_user } from '@/services/api'
import { onMounted, ref } from 'vue'

const users = ref([])
const dialog = ref(false)

const d_title = ref('')
const d_text = ref('')

onMounted(() => {
  getUsers()
})

const createUser = async (payload) => {
  try {
    const response = await new_user(payload)
    if (response.data) {
      d_text.value = 'User successfully create'
      d_title.value = 'Message'
      dialog.value = true
      getUsers()
    }
  } catch (error) {
    d_text.value = error.message
    d_title.value = 'Error'
    dialog.value = true
  }
}
const getUsers = async () => {
  try {
    const result = await get_users()

    if (result.data) users.value.splice(0, users.value.length, ...result.data)
  } catch (error) {
    console.log(error)
  }
}

const deleteUser = (id) => {
  console.log(id)
}

const editUser = (id) => {
  console.log(id)
}
</script>
