/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2014-06-16 15:27:02                          */
/*==============================================================*/


drop table if exists tbl_candidate;

drop table if exists tbl_candidate_positon;

drop table if exists tbl_customer;

drop table if exists tbl_hunter;

drop table if exists tbl_hunter_position;

drop table if exists tbl_position;

drop table if exists tbl_position_trace;

drop table if exists tbl_resume;

drop table if exists tbl_staff;

/*==============================================================*/
/* Table: tbl_candidate                                         */
/*==============================================================*/
create table tbl_candidate
(
   id                   bigint not null,
   name                 varchar(20) not null,
   email                varchar(100),
   phone                varchar(20),
   qq                   varchar(20),
   degree               varchar(10),
   school               varchar(50),
   resume               int not null,
   onjob                boolean,
   input_date           datetime not null,
   primary key (id)
);

/*==============================================================*/
/* Table: tbl_candidate_positon                                 */
/*==============================================================*/
create table tbl_candidate_positon
(
   id                   bigint not null,
   positon_id           bigint not null,
   candidate_id         bigint not null,
   primary key (id)
);

/*==============================================================*/
/* Table: tbl_customer                                          */
/*==============================================================*/
create table tbl_customer
(
   id                   bigint not null auto_increment,
   name                 varchar(100) not null,
   industy              varchar(100) not null,
   contact              varchar(50) not null,
   phone                varchar(50) not null,
   address              varchar(100),
   cust_service         varchar(50),
   level                varchar(1) not null,
   sts                  varchar(1) not null,
   reg_date             datetime not null,
   primary key (id)
);

/*==============================================================*/
/* Table: tbl_hunter                                            */
/*==============================================================*/
create table tbl_hunter
(
   id                   bigint not null,
   name                 varchar(50) not null,
   qq                   varchar(20),
   email                varchar(60) not null,
   phone                varchar(50) not null,
   level                varchar(1) not null,
   tags                 varchar(200),
   sts                  varchar(1) not null,
   reg_date             datetime not null,
   primary key (id)
);

/*==============================================================*/
/* Table: tbl_hunter_position                                   */
/*==============================================================*/
create table tbl_hunter_position
(
   id                   bigint not null auto_increment,
   position_id          bigint not null,
   hunter_id            bigint not null,
   primary key (id)
);

/*==============================================================*/
/* Table: tbl_position                                          */
/*==============================================================*/
create table tbl_position
(
   id                   bigint not null,
   name                 varchar(100) not null,
   type                 varchar(2) not null,
   base                 varchar(50) not null,
   jobtype              varchar(20) not null,
   experience_required  varchar(50) not null,
   degree_required      varchar(50) not null,
   office_address       varchar(200) not null,
   resume_achieve_email varchar(200) not null,
   description          text not null,
   keywords             varchar(100) not null,
   create_date          datetime not null,
   publish_date         datetime,
   update_date          datetime,
   primary key (id)
);

/*==============================================================*/
/* Table: tbl_position_trace                                    */
/*==============================================================*/
create table tbl_position_trace
(
   id                   bigint not null,
   positon_id           bigint not null,
   operator_id          bigint not null,
   operator_type        varchar(20) not null,
   operation            varchar(200) not null,
   update_date          datetime not null,
   primary key (id)
);



/*==============================================================*/
/* Table: tbl_resume                                            */
/*==============================================================*/
create table tbl_resume
(
   id                   bigint not null,
   url                  varchar(500),
   primary key (id)
);

/*==============================================================*/
/* Table: tbl_staff                                             */
/*==============================================================*/
create table tbl_staff
(
   id                   bigint not null auto_increment,
   primary key (id)
);

alter table tbl_candidate add constraint FK_Reference_6 foreign key (resume)
      references tbl_resume (id) on delete restrict on update restrict;

alter table tbl_candidate_positon add constraint FK_Reference_3 foreign key (candidate_id)
      references tbl_candidate (id) on delete restrict on update restrict;

alter table tbl_candidate_positon add constraint FK_Reference_4 foreign key (positon_id)
      references tbl_position (id) on delete restrict on update restrict;

alter table tbl_hunter_position add constraint FK_Reference_1 foreign key (position_id)
      references tbl_position (id) on delete restrict on update restrict;

alter table tbl_hunter_position add constraint FK_Reference_2 foreign key (hunter_id)
      references tbl_hunter (id) on delete restrict on update restrict;

alter table tbl_position_trace add constraint FK_Reference_5 foreign key (positon_id)
      references tbl_position (id) on delete restrict on update restrict;

