<template>
  <v-table height="300px" fixed-header>
    <thead>
      <tr>
        <th class="text-center">Username</th>
        <th class="text-center">Roles</th>
        <th class="text-center">Timezone</th>
        <th class="text-center">Is Active?</th>
        <th class="text-center">Last Updated At</th>
        <th class="text-center">Created At</th>
        <th class="text-center">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user._id">
        <td>{{ user.username }}</td>

        <!-- Roles -->
        <td>
          <span v-for="(role, index) in user.roles" :key="index"
            >{{ role }}
            <span v-if="index < user.roles.length - 1">, </span>
          </span>
        </td>
        <!--  -->
        <td>{{ user.preferences.timezone }}</td>
        <td>{{ user.active }}</td>
        <td>{{ user.updated_ts ? formatDate(user.updated_ts) : '' }}</td>
        <td>{{ formatDate(user.created_ts) }}</td>

        <td>
          <div class="d-flex">
            <v-btn
              icon="mdi-pencil-box"
              variant="plain"
              @click="emit('edit-user', user._id)"
            ></v-btn>
            <v-btn
              icon="mdi-delete-circle"
              variant="plain"
              @click="emit('delete-user', user._id)"
            ></v-btn>
          </div>
        </td>
      </tr>
    </tbody>
  </v-table>
</template>

<script setup>
defineProps({
  users: {
    type: Array,
    require: true,
  },
})

const emit = defineEmits(['edit-user', 'delete-user'])
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
</script>
