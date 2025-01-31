<template>
  <v-row>
    <v-col class="text-center">
      <UserFormComponent @new-user="createUser" />
      <UserTableComponent :users="users" @delete-user="deleteUser" @edit-user="editUser" />

      <DialogComponet :dialog="dialog" :text="d_text" :title="d_title" @close="dialog = false" />

      <ConfirmDialogComponent
        :dialog="confirm"
        :del="delUser"
        :text="d_text"
        :title="d_title"
        @close="confirm = false"
        @confirm="updateUser"
        @confirm-delete="confirmDelete"
      />
    </v-col>
  </v-row>
</template>

<script setup>
import ConfirmDialogComponent from '@/components/ConfirmDialogComponent.vue'
import DialogComponet from '@/components/DialogComponet.vue'
import UserFormComponent from '@/components/UserFormComponent.vue'
import UserTableComponent from '@/components/UserTableComponent.vue'
import { get_users, new_user, update_user, user_delete } from '@/services/api'
import { onMounted, ref } from 'vue'

const users = ref([])
const user = ref({})
const dialog = ref(false)
const confirm = ref(false)
const delUser = ref(false)

const d_title = ref('')
const d_text = ref('')

onMounted(() => {
  getUsers()
})

const createUser = async (payload) => {
  try {
    const response = await new_user(payload)
    if (response.data) {
      d_text.value = response.data.msg
      d_title.value = 'Message'
      dialog.value = true
      getUsers()
    }
  } catch (error) {
    handleError(error)
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
const editUser = (payload) => {
  user.value = payload
  d_text.value = 'Update confirm'
  d_title.value = 'Confirm action'
  confirm.value = true
  dialog.value = false
}
const updateUser = async () => {
  try {
    const id = user.value._id
    delete user.value._id

    const response = await update_user(id, user.value)

    if (response.data) {
      d_text.value = response.data.msg
      d_title.value = 'Message'
      dialog.value = true
      confirm.value = false

      getUsers()
    }
  } catch (error) {
    handleError(error)
  }
}
const handleError = (error) => {
  d_text.value = error.message
  d_title.value = 'Error'
  dialog.value = true
}

const deleteUser = (id) => {
  user.value = id
  d_text.value = 'Delete confirm'
  d_title.value = 'Confirm action'
  confirm.value = true
  dialog.value = false
  delUser.value = true
}

const confirmDelete = async () => {
  try {
    const response = await user_delete(user.value)

    if (response.data) {
      d_text.value = response.data.msg
      d_title.value = 'Message'
      dialog.value = true
      confirm.value = false
      delUser.value = false

      getUsers()
    }
  } catch (error) {
    handleError(error)
    delUser.value = false
  }
}
</script>
