create table user_details(email_id varchar(30) primary key, password varchar(15) not null, name varchar(30) 
not null, gender char(1) not null,  mobile varchar(14) not null, city varchar(20) not null,
state varchar(25) not null,CHECK(gender='M' or gender='F'));

create table station(station_id varchar(8) primary key, station_name varchar(25));

create table train(train_id varchar(10) primary key, train_name varchar(50) not null, train_type varchar(50) not null, 
source_id varchar(8), dest_id varchar(8), seats int not null,
fare int not null,foreign key(source_id) 
references station(station_id) on update cascade on delete cascade, foreign key(dest_id) references station(station_id) 
on update no action on delete no action);

create table train_status(train_id varchar(10), available_date varchar(20), booked_seats int,
 available_seat int, primary key(train_id,available_date),foreign key(train_id) references train(train_id) 
 on update cascade on delete cascade);
 
insert into user_details values('dubey@yahoo.co.in','abcd123','Abhishek Dubey','M','9567483902','Bhopal','Madhya Pradesh');
insert into user_details values('jeevan@gmail.com','vcgd111','Jeevan Arra','M','9567483989','Mumbai','Maharashtra');
insert into user_details values('aaleya15@yahoo.com','fhgkkk181','Chaitali Biswas','F','9574839758','Kolkata','West Bengal');
insert into user_details values('himanshu104@yahoo.com','vgfdf1616','Himanshu Mishra','M','9797483902','Vishakapatnam','Andhra Pradesh');
insert into user_details values('deena.josphine1985@gmail.com','9739gdf','Deena Josphine','F','9475839759','Mangalore','Karnataka');
 
insert into station values('DDN','Dehradun');
insert into station values('BDTS','Bandra Terminus');
 
insert into train values(19020,'Dehradun Express','Express','DDN','BDTS',200,700);
insert into train values(12431,'Rajdhani Express','Express','TVC','NZM',200,800);
insert into train values(12010,'Shatabdi Express','Express','ADI','BCT',200,1025);
insert into train values(15008,'LJN BCY Express','Express','LJN','BCY',75,256);
insert into train values(11464,'JBP Somnath Express','Express','JBP','SMNH',75,520);

insert into train_status values(19020, '27/11/2017', 0, 200);

create table user_bookings(email_id varchar(30) primary key,source_id varchar(30) not null,dest_id varchar(30) not null,train_id varchar(10) not null,no_of_seats varchar(1),foreign key(dest_id) references station(station_id),foreign key(source_id) references station(station_id),foreign key(train_id) references train(train_id));


GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA PUBLIC TO pooja;
