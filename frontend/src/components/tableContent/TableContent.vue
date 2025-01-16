<template>
    <v-table
      height="700"
      fixed-header
      class="table"
    >
      <thead>
        <tr>
          <th class="text-left">
            Username
          </th>
          <th class="text-left">
            Roles
          </th>
          <th class="text-left">
            Timezone
          </th>
          <th class="text-left">
            Is Active?
          </th>
          <th class="text-left">
            Last Updated At
          </th>
          <th class="text-left">
            Created At
          </th>
          <th class="text-left">
            Actions
          </th>
        </tr>
      </thead>
      <tbody class="text-left">
        <tr
          v-for="user in users"
          :key="user._id"
        >
          <td>
            <router-link :to="`/user/${user._id}`">{{ user.username }}</router-link>
          </td>

          <td>
            <span v-for="(role, index) in user.roles" :key="index">{{ role }}
              <span v-if="index < user.roles.length - 1">, </span>
            </span>
            
          </td> 
          <td>{{ user.preferences.timezone }}</td>
          <td>{{ user.active }}</td>
          <td> {{ user.updated_ts ? formatDate(user.updated_ts) : '' }} </td>
          <td>{{ formatDate(user.created_ts) }}</td>
          <td>
            <router-link :to="`/user/${user._id}?isEditable=true`">
              <v-btn
              >
              <i class="bi bi-pencil-square"></i>
              </v-btn>
             
            </router-link>

              <v-btn
              @click="emitId(user._id)"
              >
              <i class="bi bi-trash3-fill"></i>
            </v-btn>
          </td>
          
        </tr>
      </tbody>
    </v-table>

  
  </template>
  
  
  <script>

export default {
    emits:['delete-user'],
    name: 'TableContent',
    components:{
  
    },
    data(){
      return{
        userId: ''
      }
    },
    props:{
        users:{
            type: Array,
            required: true
        },
    },
    methods:{
      emitId(id){
        this.$emit('delete-user', id)

      },
      formatDate(timestamp) {
      const date = new Date(timestamp * 1000); 
      const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        hour12: true,
      };

      return date.toLocaleDateString('en-US', options); // US Format
    },
    }
}
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  